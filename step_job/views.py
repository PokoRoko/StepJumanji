from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import (HttpResponseBadRequest, HttpResponseForbidden,
                         HttpResponseNotFound, HttpResponseServerError)
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, FormView, View
from django.contrib.auth.decorators import login_required

from .forms import ApplicationForm, PostcardForm
from .models import Company, Specialty, Vacancy, Application,Resume


def custom_handler400(request, exception):
    return HttpResponseBadRequest(f'Неверный запрос!\n{exception}')


def custom_handler403(request, exception):
    return HttpResponseForbidden(f'Доступ запрещен!\n{exception}')


def custom_handler404(request, exception):
    return HttpResponseNotFound(f'Ресурс не найден!\n{exception}')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialty"] = Specialty.objects.annotate(count=Count("vacancies"))
        context["companies"] = Company.objects.annotate(count=Count("vacancies"))
        return context


class ListVacanciesView(LoginRequiredMixin,ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Все вакансии"
        return context


class ListSpecializationView(LoginRequiredMixin,ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies.html"

    def get_queryset(self):
        return self.model.objects.filter(specialty__code=self.kwargs['specialty']).select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = self.kwargs['specialty'].title
        return context


class DetailCompanyViews(LoginRequiredMixin, DetailView):
    model = Company
    context_object_name = "company"
    template_name = "company.html"

    def get_queryset(self):
        return self.model.objects.prefetch_related("vacancies", "vacancies__specialty")


class VacancyView(LoginRequiredMixin, View):

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationForm()
        return render(
            request,
            template_name="vacancy.html",
            context={
                "vacancy": vacancy,
                "form": form})

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.user = request.user
            application.save()
            return redirect('sent')  # Не работает нужно добавить reverse

        return render(
            request,
            template_name="vacancy.html",
            context={
                "vacancy": vacancy,
                "form": form})


# New week
class SentView(LoginRequiredMixin, TemplateView):
    template_name = "sent.html"


class MyCompanyView(LoginRequiredMixin, DetailView):
    template_name = "company-edit.html"
    model = Company
    context_object_name = "company"
    queryset = model.objects.select_related("owner")


class ListMyVacanciesView(LoginRequiredMixin, ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy-list.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Мои вакансии"
        return context


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    context_object_name = "company"
    template_name = "company-edit.html"
    queryset = model.objects.select_related("specialty", "company")


class CreateVacancyView(LoginRequiredMixin, CreateView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy-edit.html"
    # queryset = model.objects.select_related("vacancies", "vacancies__specialty")
