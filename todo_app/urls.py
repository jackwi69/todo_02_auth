from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.create_task, name="create_task"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('upgrade/<int:pk>/', views.upgrade, name="upgrade"),
]
