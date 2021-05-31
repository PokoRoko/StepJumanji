from django.urls import path

from .views import (companies_view, custom_handler400, custom_handler403,
                    custom_handler404, custom_handler500, index_view,
                    specialization_view, vacancies_view, vacancy_view)

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', index_view, name="main"),
    path('vacancies/', vacancies_view, name="vacancies"),
    path('vacancies/cat/<str:name_spec>/', specialization_view, name="specialization"),
    path('companies/<int:id_company>/', companies_view, name="companies"),
    path('vacancies/<int:id_vacancy>/', vacancy_view, name="vacancy"),
]
