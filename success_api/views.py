from django.http import HttpResponse
from rest_framework import generics

from success_api.serializers import CreateOrUpdateSuccessGradeAnswerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CreateOrUpdateSuccessGradeAnswerView(generics.CreateAPIView):
    serializer_class = CreateOrUpdateSuccessGradeAnswerSerializer
