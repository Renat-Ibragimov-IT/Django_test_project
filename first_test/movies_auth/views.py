from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import SignUpUserForm, LoginUserForm, ProfileUserForm


def home(request):
    return render(request, "movies_auth/home.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy("")
    template_name = "registration/login.html"


def sign_up_user(request):
    s_form = SignUpUserForm()
    p_form = ProfileUserForm()
    if request.method == "POST":
        s_form = SignUpUserForm(request.POST)
        p_form = ProfileUserForm(request.POST)
        if s_form.is_valid() and p_form.is_valid():
            new_user = s_form.save()
            profile = p_form.save(commit=False)
            profile.user = new_user
            profile.save()
            return redirect('login')

    context = {'pform': p_form, 'sform': s_form}
    return render(request, 'registration/signup.html', context)
