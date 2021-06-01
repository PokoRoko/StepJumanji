from django.urls import path

from .views import custom_handler400, custom_handler403, custom_handler404, custom_handler500, IndexView,DetailVacancyView,DetailCompanyViews,ListVacanciesView,ListSpecializationView

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/cat/<str:name_spec>/', ListSpecializationView.as_view(), name="specialization"),
    path('companies/<int:id_company>/', DetailCompanyViews.as_view(), name="companies"),
    path('vacancies/<int:id_vacancy>/', DetailVacancyView.as_view(), name="vacancy"),
]
