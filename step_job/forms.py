
from .models import Application
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# class PostcardForm(forms.Form):
#     address = forms.CharField(label='Destination Address')
#     author = forms.CharField(min_length=3)
#     compliment = forms.CharField(max_length=1024)
#     date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
#     email = forms.EmailField()


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))