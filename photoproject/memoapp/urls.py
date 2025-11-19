from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    path('create/', views.memo_create, name='memo_create'),
    path('<int:pk>/delete/', views.memo_delete, name='memo_delete'), 
]