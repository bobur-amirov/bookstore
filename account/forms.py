from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


class AccountEditForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'img', 'bio', 'birth_date', 'phone']