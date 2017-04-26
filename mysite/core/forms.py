from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LandOwnerSignUpForm(UserCreationForm):
    lat = forms.FloatField(min_value=-90.0, max_value=90.0)
    lon = forms.FloatField(min_value=-180.0, max_value=180.0)
    email = forms.EmailField(help_text='yourname@example.com')
    pincode = forms.IntegerField()
    place = forms.CharField()
    slots = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class CarOwnerSignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='yourname@example.com')
    name = forms.CharField()
    phone = forms.IntegerField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )
