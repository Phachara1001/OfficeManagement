from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login',views.go_login),
    path('add_drug',views.add_drug),
    path('manage_drug',views.manage_drug),
    path('delete/<int:pk>',views.delete_drug),
]