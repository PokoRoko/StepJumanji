import datetime

from django.contrib.messages.views import SuccessMessageMixin
from loguru import logger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import (HttpResponseBadRequest, HttpResponseForbidden,
                         HttpResponseNotFound, HttpResponseServerError)
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, FormView, View
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from step_job.forms import ApplicationForm, CompanyForm, VacancyForm
from step_job.models import Company, Specialty, Vacancy, Application, Resume


def custom_handler400(request, exception):
    return HttpResponseBadRequest(f'Неверный запрос!\n{exception}')


def custom_handler403(request, exception):
    return HttpResponseForbidden(f'Доступ запрещен!\n{exception}')


def custom_handler404(request, exception):
    return HttpResponseNotFound(f'Ресурс не найден!\n{exception}')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


class IndexView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialty"] = Specialty.objects.annotate(count=Count("vacancies"))
        context["companies"] = Company.objects.annotate(count=Count("vacancies"))
        return context


class ListVacanciesView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy/vacancies.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Все вакансии"
        return context


class ListSpecializationView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy/vacancies.html"

    def get_queryset(self):
        return self.model.objects.filter(specialty__code=self.kwargs['specialty']).select_related("specialty",
                                                                                                  "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = self.kwargs['specialty'].title
        return context


class DetailCompanyViews(DetailView):
    model = Company
    context_object_name = "company"
    template_name = "company/company.html"

    def get_queryset(self):
        return self.model.objects.prefetch_related("vacancies", "vacancies__specialty")


class SendView(LoginRequiredMixin, TemplateView):
    template_name = "base/sent.html"


class VacancyView(View):

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationForm()
        return render(
            request,
            template_name="vacancy/vacancy.html",
            context={
                "vacancy": vacancy,
                "form": form})

    def post(self, request, pk):  # Отсечку авторизации сделал через шаблон
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.user = request.user
            application.save()
            return redirect('send/')

        return render(
            request,
            template_name="vacancy/vacancy.html",
            context={
                "vacancy": vacancy,
                "form": form})


class MyCompanyView(LoginRequiredMixin, View):

    def get(self, request):
        my_company = get_object_or_404(Company, owner__username=request.user)
        if my_company:
            form = CompanyForm(instance=my_company)
            return render(
                request,
                template_name="company/company-edit.html",
                context={
                    "company": my_company,
                    "form": form})

        else:
            return render(
                request,
                template_name="company/company-create.html",
                context={
                    "company": my_company,
                })

    def post(self, request):
        info_update = "Информация о компании обновлена"
        my_company = Company.objects.get(owner__username=request.user)
        form = CompanyForm(request.POST, instance=my_company)
        if form.is_valid():
            my_company = form.save(commit=False)
            my_company.owner = self.request.user
            my_company.save()

        return render(
            request,
            template_name="company/company-edit.html",
            context={
                'info_update': info_update,
                "company": my_company,
                "form": form})


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    context_object_name = "company"
    template_name = "company/company-edit.html"
    queryset = model.objects.select_related("specialty", "company")
    fields = [
        "name",
        "location",
        "logo",
        "description",
        "employee_count",
    ]


class ListMyVacanciesView(LoginRequiredMixin, ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy/vacancy-list.html"

    # queryset = model.objects.select_related("specialty", "company")

    def get_queryset(self):
        return self.model.objects.filter(company__owner=self.request.user, ).select_related("company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Мои вакансии"
        return context


class CreateVacancyView(LoginRequiredMixin, CreateView):
    context_object_name = "vacancy"
    template_name = "vacancy/vacancy-edit.html"
    form_class = VacancyForm
    success_message = 'Вакансия создана!'

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.get(owner__username=self.request.user)
            vacancy.published_at = datetime.datetime.now()
            vacancy.save()
        return redirect('/')


class UpdateVacancyView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vacancy
    context_object_name = "vacancy"
    template_name = "vacancy/vacancy-edit.html"
    form_class = VacancyForm
    success_url = "/mycompany/vacancies/8/"
    success_message = "Данные вакансии обновлены!"
    pk_url_kwarg = "pk"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["applications"] = Application.objects.filter(vacancy="vacancy.id")
    #     return context
