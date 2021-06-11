from django.db.models import Count
from django.http import (HttpResponseBadRequest, HttpResponseForbidden,
                         HttpResponseNotFound, HttpResponseServerError)
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, FormView, View
from django.contrib.auth.decorators import login_required


from .models import Company, Specialty, Vacancy


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


class ListVacanciesView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Все вакансии"
        return context

class ListSpecializationView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies.html"

    def get_queryset(self):
        return self.model.objects.filter(specialty__code=self.kwargs['specialty']).select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = self.kwargs['specialty'].title
        return context


class DetailCompanyViews(DetailView):
    model = Company
    context_object_name = "company"
    template_name = "company.html"

    def get_queryset(self):
        return self.model.objects.prefetch_related("vacancies", "vacancies__specialty")


class DetailVacancyView(DetailView):
    template_name = "vacancy.html"
    model = Vacancy
    context_object_name = "vacancy"
    queryset = model.objects.select_related("specialty", "company")


# New week
class SentView(TemplateView):
    template_name = "sent.html"


class DetailViewMyCompany(DetailView):
    template_name = "company-edit.html"
    model = Company
    context_object_name = "company"
    queryset = model.objects.select_related("owner")


class ListMyVacanciesView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy-list.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Мои вакансии"
        return context


class CreateCompanyView(CreateView):
    model = Company
    context_object_name = "company"
    template_name = "company-edit.html"
    queryset = model.objects.select_related("specialty", "company")


class CreateVacancyView(CreateView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancy-edit.html"
    # queryset = model.objects.select_related("vacancies", "vacancies__specialty")
