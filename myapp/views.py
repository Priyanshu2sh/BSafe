from django.shortcuts import render

from .streamlit import detect_safety_gear
from .serilaizers import ImageUploadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.core.files.base import ContentFile


# Create your views here.

class ImageUploadAPI(APIView):
    def post(self, request):

        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image_base64 = serializer.validated_data["image_base64"]
            
            # Strip header if exists
            if "base64," in image_base64:
                _, image_base64 = image_base64.split("base64,", 1)

            try:
                decoded_image = base64.b64decode(image_base64)
            except Exception:
                return Response(
                    {"error": "Invalid base64 data."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Run detection
            result = detect_safety_gear(decoded_image)

            return Response(
                {
                    "detected_items": result["detected_items"],
                    "detection_checklist": result["detection_checklist"],
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)