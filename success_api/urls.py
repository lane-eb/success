from django.urls import path

from success_api import views

urlpatterns = [
    path('', views.index, name='index'),
]
