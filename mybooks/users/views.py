from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from django.db.models import Q

from .forms import UserCreationForm
from .models import User

class RegisterUser(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile:profile')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class AllUsersView(ListView):
    model = User
    template_name = 'users/all_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(~Q(username=self.request.user))