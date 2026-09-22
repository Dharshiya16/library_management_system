from django.urls import path
from . import views


urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.member_add, name='member_add'),
    path('edit/<int:id>/', views.member_edit, name='member_edit'),
    path('delete/<int:id>/', views.member_delete, name='member_delete'),
]