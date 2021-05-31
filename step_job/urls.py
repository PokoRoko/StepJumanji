from django.urls import path

from .views import  custom_handler400, custom_handler403, custom_handler404, custom_handler500, IndexView,DetailVacancyView,DetailCompanyViews,ListVacanciesView,ListSpecializationView

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', IndexView, name="main"),
    path('vacancies/', ListVacanciesView, name="vacancies"),
    path('vacancies/cat/<str:name_spec>/', ListSpecializationView, name="specialization"),
    path('companies/<int:id_company>/', DetailCompanyViews, name="companies"),
    path('vacancies/<int:id_vacancy>/', DetailVacancyView, name="vacancy"),
]
