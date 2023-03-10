from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 
            'email',
            'first_name',
            'last_name',
            'bio_content',
            'photo_url',
        ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 
            'email',    
            'first_name',
            'last_name',
            'bio_content',
            'photo_url',
        ]
