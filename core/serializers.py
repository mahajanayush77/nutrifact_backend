from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)