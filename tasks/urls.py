from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('complete/<int:id>/', views.task_complete, name='task_complete'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
]
