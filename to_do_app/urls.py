
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.TaskListview.as_view(),name='task_list'),
    path('task/create/',views.TaskCreateView.as_view(),name='task_create'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='task_delete'), # type: ignore
    path('tasks/finish/<int:task_id>/', views.finish_task, name='task_finish'), # type: ignore

]