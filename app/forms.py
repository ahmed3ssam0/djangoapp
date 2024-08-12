from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class CreateOrderUser(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'status']

    def __init__(self, *args, **kwargs):
        super(CreateOrderUser, self).__init__(*args, **kwargs)
        self.fields['status'].initial = 'Pending'
        self.fields['status'].widget = forms.HiddenInput()
        # self.fields['status'].disabled = True