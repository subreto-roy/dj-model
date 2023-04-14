from django import forms
from django.core import validators

def start_with_S(value):
    if value[0] != 's':
        raise forms.ValidationError('error')
    
    
class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[start_with_S])
    email = forms.EmailField(validators=[start_with_S])
    #password = forms.CharField(widget=forms.PasswordInput)
    # key = forms.CharField(widget=forms.HiddenInput())

    # def clean_name(self):
    #     valname = self.changed_data['name']
    #     if len(valname) < 4:
    #         raise forms.ValidationError('Enter more than or equal 4')
    #     return valname
