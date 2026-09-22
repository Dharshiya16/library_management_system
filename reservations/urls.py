from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('add/', views.reservation_add, name='reservation_add'),
    path('delete/<int:id>/', views.reservation_delete, name='reservation_delete'),
    path('edit/<int:id>/', views.reservation_edit, name='reservation_edit'),
]