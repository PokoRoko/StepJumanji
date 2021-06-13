from django.urls import path

from .views.views import (CreateCompanyView, CreateVacancyView,
                          DetailCompanyViews, IndexView, ListMyVacanciesView,
                          ListSpecializationView, ListVacanciesView,
                          MyCompanyView, SendView, UpdateVacancyView,
                          VacancyView, custom_handler400, custom_handler403,
                          custom_handler404, custom_handler500)

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # Вакансии
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/<int:pk>/', VacancyView.as_view(), name="vacancy"),
    path('vacancies/cat/<str:specialty>/', ListSpecializationView.as_view(), name="specialization"),
    path('vacancies/<int:pk>/send/', SendView.as_view(), name="send"),
    # Компании
    path('companies/<int:pk>/', DetailCompanyViews.as_view(), name="company"),
    path('mycompany/', MyCompanyView.as_view(), name="my_company"),
    path('mycompany/letsstart/', MyCompanyView.as_view(), name="company_lets_start"),
    path('mycompany/create/', CreateCompanyView.as_view(), name="my_company_create"),
    # Создание вакансий
    path('mycompany/vacancies/', ListMyVacanciesView.as_view(), name="list_my_vacancies"),
    path('mycompany/vacancies/create/', CreateVacancyView.as_view(), name="my_vacancy_create"),
    path('mycompany/vacancies/<int:pk>/', UpdateVacancyView.as_view(), name='my_vacancy_edit'),
]
