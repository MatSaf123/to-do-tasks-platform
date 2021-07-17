from django.urls import path
from .views import TaskCreate, TaskUpdate, TaskDelete, TaskDetail, TaskList, task_change_status

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-change-status/<int:pk>/', task_change_status, name='task-change-status'),
]