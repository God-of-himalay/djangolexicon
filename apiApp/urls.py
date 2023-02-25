from django.urls import path
from . import views

urlpatterns = [
    path('my-api/', views.my_api, name='my_api'),
]


