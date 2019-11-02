from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='First Name')
    email = forms.CharField(max_length=30, label='Last Name')
    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()
        return user
    
