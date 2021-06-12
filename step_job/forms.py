from django.utils.translation import gettext_lazy as _
from .models import Application
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostcardForm(forms.Form):
    address = forms.CharField(label='Destination Address')
    author = forms.CharField(min_length=3)
    compliment = forms.CharField(max_length=1024)
    date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
    email = forms.EmailField()


class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

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
        labels = {
            "written_username": _('Ваше имя'),
            "written_phone": _('Телефон'),
            "written_cover_letter": _('Сопроводительное письмо'),
        }
        help_texts = {
            "written_username": _('Укажите как к вам обращаться'),
        }