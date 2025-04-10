from django.db import models
from config.settings import AUTH_USER_MODEL

# Create your models here.
class Task(models.Model):
    STATUS_NOT_DONE = 'n'
    STATUS_DONE = 'd'
    TASK_STATUS = [
        (STATUS_NOT_DONE,'In Progress'),
        (STATUS_DONE,'done')
    ]
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,)
    description = models.CharField(max_length=255,blank=False,null=False)
    status = models.CharField(max_length=1,default=STATUS_NOT_DONE,choices=TASK_STATUS)
    date_time_created = models.DateTimeField(auto_now_add=True)