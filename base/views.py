from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):

    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        # Get only logged-in user tasks
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_completed=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):

    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):

    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """Set currently logged in user as the author"""
        
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):

    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):

    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')