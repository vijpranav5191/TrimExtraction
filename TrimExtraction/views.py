from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpRequest
from django.core import serializers
from django.conf import settings
import json
from TrimExtraction.Services import services
from TrimExtraction.Logging import logger


# Create your views here.

@api_view(["GET"])
def TestEndPoint(self):
    return JsonResponse("Api Response", safe = False)

@api_view(["POST"])
def ReceiveImage(request):
    data = request.data
    imageName = str(data.get("image"))
    imageId = logger.log_msg(action="Received",imageName=imageName)
    receivedImage = data.get("image",False).read()
    trimInformation = services.process_image(receivedImage, imageId, imageName)
    return JsonResponse({'Trim_Information': trimInformation})
