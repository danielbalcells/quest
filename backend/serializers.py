from rest_framework import serializers

from backend import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'text', 'created')


class QuestionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionLink
        fields = ('id', 'source', 'target')

    def create(self, validated_data):
        return models.QuestionLink(**validated_data)
