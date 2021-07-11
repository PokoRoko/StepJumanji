from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Application, Company, Vacancy


class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Оставить отклик'))

    class Meta:
        model = Application
        fields = [
            "written_username",
            "written_phone",
            "written_cover_letter",
        ]
        exclude = [
            "vacancy",
            "user",
        ]
        help_texts = {
            "written_username": _('Укажите как к вам обращаться'),
        }


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Company
        fields = [
            "name",
            "location",
            "logo",
            "description",
            "employee_count",
        ]
        exclude = [
            "owner",
        ]
        help_texts = {
            "location": _('Укажите город или страну'),
        }


class VacancyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить вакансию'))

    class Meta:
        model = Vacancy
        fields = [
            "title",
            "specialty",
            "skills",
            "description",
            "salary_min",
            "salary_max",
        ]
        exclude = [
            "company",
            "published_at",
        ]
