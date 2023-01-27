from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.index, name='index'),
    path('rest/', views.ph_data, name='rest'),
]