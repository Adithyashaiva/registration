from django import forms
from .models import Registration
from datetime import date

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'date_of_birth', 'gender', 'age']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob