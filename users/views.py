from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.

class CustomLoginView(LoginView):

    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
        
class CustomLogoutView(LogoutView):

    next_page = 'login'

class RegisterView(FormView):

    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        """If user is already logged in, redirect him to Tasks page."""

        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)