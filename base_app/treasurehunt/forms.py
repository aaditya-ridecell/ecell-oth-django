from django import forms
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter the Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Reenter the password"})
    )

    class Meta:
        model = models.UserProfile
        fields = ("email", "password", "confirm_password")


class Answer(forms.ModelForm):
    answer = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Answer"}))

    class Meta:
        model = models.Answer
        fields = ("answer",)
