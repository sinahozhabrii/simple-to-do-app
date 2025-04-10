from django.forms import ModelForm
from . import models

class TaskAddForm(ModelForm):
    class Meta:
        model = models.Task
        fields = ['description']