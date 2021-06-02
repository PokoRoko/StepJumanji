from django.urls import path

from .views import (DetailCompanyViews, DetailVacancyView, IndexView,
                    ListSpecializationView, ListVacanciesView,
                    custom_handler400, custom_handler403, custom_handler404,
                    custom_handler500)

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/cat/<str:specialty>/', ListSpecializationView.as_view(), name="specialization"),
    path('companies/<int:pk>/', DetailCompanyViews.as_view(), name="company"),
    path('vacancies/<int:pk>/', DetailVacancyView.as_view(), name="vacancy"),
]
