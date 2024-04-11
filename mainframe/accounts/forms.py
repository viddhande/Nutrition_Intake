from django import forms

class UserInputForm(forms.Form):
    dietary_preference = forms.CharField(max_length=100)
    lifestyle = forms.CharField(max_length=100)
    health_condition = forms.CharField(max_length=100)
    existing_allergies = forms.CharField(max_length=100)
