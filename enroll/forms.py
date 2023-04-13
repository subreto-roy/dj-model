from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # key = forms.CharField(widget=forms.HiddenInput())

    def clean_name(self):
        valname = self.changed_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than or equal 4')
        return valname
