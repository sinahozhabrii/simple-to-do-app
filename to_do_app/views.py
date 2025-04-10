from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from . import models
from . import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskListview(LoginRequiredMixin,ListView):
    model = models.Task
    template_name = 'to_do_app/to_do_list.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        return super().get_queryset().filter(status='n')
    
class TaskCreateView(CreateView):
    model = models.Task
    form_class = forms.TaskAddForm
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)
    
def delete_task(request,task_id):
    if request.method == "POST":
        task = get_object_or_404(models.Task,pk=task_id)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return JsonResponse({'status': 'success'})
    
def finish_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(models.Task, id=task_id)
        task.status = 'd'  
        task.save()
        messages.success(request, 'Task marked as finished!')
        return JsonResponse({'status': 'success'})
