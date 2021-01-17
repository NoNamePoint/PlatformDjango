from django.forms import ModelForm
# Форма регистрации пользоватлеля
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # дефолтная модель пользователя
from django import forms

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order 
        fields = '__all__'  # 'Автоматом получаем все поля модели'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

