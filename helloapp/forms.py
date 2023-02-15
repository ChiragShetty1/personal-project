from django import forms
from helloapp.models import Forms

class con_form(forms.ModelForm):
    class Meta:
        model=Forms
        fields='__all__'
