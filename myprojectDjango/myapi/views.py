from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def sample_api(request):
    return JsonResponse({"message": "Hello, Django API is running Ismail!"})
