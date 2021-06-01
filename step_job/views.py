from django.http import (HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)

from django.db.models import Count
from django.views.generic import ListView,DetailView,TemplateView

from .models import Company, Vacancy, Specialty


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
    context_object_name = "vacancy"
    queryset = model.objects.select_related("specialty", "company")
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Все вакансии"


class ListSpecializationView(ListView):
    template_name = "vacancies.html"
    model = Vacancy
    context_object_name = "vacancies"

    def get_queryset(self):
        return self.model.objects.filter(specialty__code=self.kwargs['specialty']).select_related("specialty","company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = self.kwargs['specialty']


class DetailCompanyViews(DetailView):
    template_name = "company.html"
    model = Company
    context_object_name = "company"

    def get_queryset(self):
        return self.model.objects.prefetch_related("vacancies", "vacancies__specialty")


class DetailVacancyView(DetailView):
    template_name = "vacancy.html"
    model = Vacancy
    context_object_name = "vacancy"
    queryset = model.objects.select_related("specialty", "company")


