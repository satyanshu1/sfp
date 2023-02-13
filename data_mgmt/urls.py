from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.index, name='index'),
    path('rest/', views.ph_data, name='rest'),
    path('rest/user_reg', views.user_reg, name='user_reg'),
    path('rest/user_auth', views.user_auth, name='user_auth'),
]