from .models import todo_User as todoapp_models
from django import forms
class signupform(forms.ModelForm):

    confirm_password = forms.CharField()

    class Meta:
        model= todoapp_models
        fields=['username','phone_number', 'email','password']

    def clean(self):
        cleaned_data =super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password is not matching")

        return cleaned_data

