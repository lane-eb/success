from rest_framework.fields import JSONField
from rest_framework.serializers import ModelSerializer

from success_api.models import Answer


class CreateOrUpdateSuccessGradeAnswerSerializer(ModelSerializer):
    values = JSONField(required=False)

    class Meta:
        model = Answer
        fields = ['values']

