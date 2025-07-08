from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image_base64 = serializers.CharField()
