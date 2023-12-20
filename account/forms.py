from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Эта почта уже зарегестрированна")
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
