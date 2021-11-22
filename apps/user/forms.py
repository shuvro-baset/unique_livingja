from .models import UniUser as User
from django import forms


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=20, min_length=4)
    last_name = forms.CharField(required=True, max_length=20, min_length=4)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")
