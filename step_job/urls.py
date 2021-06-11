from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (DetailCompanyViews, DetailVacancyView, IndexView,
                    ListSpecializationView, ListVacanciesView,
                    custom_handler400, custom_handler403, custom_handler404,
                    custom_handler500, SentView, DetailViewMyCompany, ListMyVacanciesView, CreateVacancyView,
                    CreateCompanyView)

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', login_required(IndexView.as_view()), name="index"),
    path('vacancies/', login_required(ListVacanciesView.as_view()), name="vacancies"),
    path('vacancies/cat/<str:specialty>/', login_required(ListSpecializationView.as_view()), name="specialization"),
    path('companies/<int:pk>/', login_required(DetailCompanyViews.as_view()), name="company"),
    path('vacancies/<int:pk>/', login_required(DetailVacancyView.as_view()), name="vacancy"),
    # New week
    path('vacancies/<int:pk>/send/', login_required(SentView.as_view()), name="sent"),
    path('mycompany/', login_required(DetailViewMyCompany.as_view()), name="my_company"),
    path('mycompany/letsstart/', login_required(DetailViewMyCompany.as_view()), name="company_lets_start"),
    path('mycompany/create/', login_required(CreateCompanyView.as_view()), name="my_company_create"),
    path('mycompany/vacancies/', login_required(ListMyVacanciesView.as_view()), name="list_my_vacancies"),
    path('mycompany/vacancies/create/', login_required(CreateVacancyView.as_view()), name="my_company_create"),
    path('mycompany/vacancies/<int:pk>/', login_required(DetailVacancyView.as_view()), name='my_vacancy'),
]
