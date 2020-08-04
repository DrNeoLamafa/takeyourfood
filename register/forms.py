
from django import forms
from django.contrib.auth.forms import UserCreationForm

from register.models import User, Rest, Courier

class SignUpForm(UserCreationForm):
  class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'role')

class LkForm(forms.ModelForm):
  class Meta:
        model = Rest
        fields = ('email',  'addres')