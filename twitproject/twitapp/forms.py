from django import forms
from . models import *

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
