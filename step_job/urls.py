from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (DetailCompanyViews, VacancyView, IndexView,
                    ListSpecializationView, ListVacanciesView,
                    custom_handler400, custom_handler403, custom_handler404,
                    custom_handler500, SentView, MyCompanyView, ListMyVacanciesView, CreateVacancyView,
                    CreateCompanyView)

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/cat/<str:specialty>/', ListSpecializationView.as_view(), name="specialization"),
    path('companies/<int:pk>/', DetailCompanyViews.as_view(), name="company"),
    path('vacancies/<int:pk>/', VacancyView.as_view(), name="vacancy"),
    # New week
    path('vacancies/<int:pk>/send/', SentView.as_view(), name="sent"),
    path('mycompany/', MyCompanyView.as_view(), name="my_company"),
    path('mycompany/letsstart/', MyCompanyView.as_view(), name="company_lets_start"),
    path('mycompany/create/', CreateCompanyView.as_view(), name="my_company_create"),
    path('mycompany/vacancies/', ListMyVacanciesView.as_view(), name="list_my_vacancies"),
    path('mycompany/vacancies/create/', CreateVacancyView.as_view(), name="my_vacancy_create"),
    path('mycompany/vacancies/<int:pk>/', VacancyView.as_view(), name='my_vacancy'),
]
