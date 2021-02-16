from django.urls import path

from success_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'answers/success-grade/',
        views.CreateOrUpdateSuccessGradeAnswerView.as_view(),
        name='create-or-update-success-grade-answer',
    ),
]
