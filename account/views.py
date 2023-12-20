from django.contrib.auth import logout
from django.shortcuts import render
from .forms import SignupForm
from django.urls import reverse_lazy
from django.views import generic


def logout_view(request):
    return render(logout(request), 'registration/logged_out.html')


class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

