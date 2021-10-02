from django import forms
from .models import User
import bcrypt

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    confirmed_pw = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput,
        }
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmed_pw")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_pw does not match"
            )

    def save(self, commit=True):
        # your logic or Save your object for example:
        pw = self.cleaned_data["password"]
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=self.cleaned_data["first_name"], last_name=self.cleaned_data["last_name"], email=self.cleaned_data["email"], password=pw_hash)
        return user