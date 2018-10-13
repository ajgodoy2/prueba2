from django import forms
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    name = forms.CharField(required=False)

    def clean_username(self):
        # Check if username is not in User collection
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("Password is too short.")
        return password

    def clean_repeat_password(self):
        repeat_password = self.cleaned_data['repeat_password']
        password = self.cleaned_data.get('password')
        if password and repeat_password != password:
            raise forms.ValidationError("Passwords do not match.")
        return repeat_password
