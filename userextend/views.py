from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.save()

        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect("home-page")
