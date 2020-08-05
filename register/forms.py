
from django import forms
from django.contrib.auth.forms import UserCreationForm

from register.models import User, Rest, Courier, Client, Food


class SignUpForm(UserCreationForm):
  class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'role')

class LkForm(forms.ModelForm):
  class Meta:
        model = Rest
        fields = ('name_res',  'addres', 'category', 'discription', 'image')
        
  def __init__(self, *args, **kwargs):
        super(LkForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
class LkFormClient(forms.ModelForm):
  class Meta:
        model = Client
        fields = ('name',  'famil', 'mobil')

class LkFormCourier(forms.ModelForm):
  class Meta:
        model = Courier
        fields = ('name',  'famil')

class LkFormFood(forms.ModelForm):
  class Meta:
        model = Food
        fields = ('name',  'price', 'category', 'image')



