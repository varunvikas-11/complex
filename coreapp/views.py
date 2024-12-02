from django.shortcuts import render
from django.http import JsonResponse,HttpResponse


def sample_get_view(request):
    return HttpResponse("OG : Once up on a time there was a gangster in peddapalli and his name Tharun Sadhar he stopped many crimes and had a great name",content_type="text/plain")   

def sample1(request):
    return JsonResponse({"message":"Hello JSON"}) 

def tharun(request):
    return HttpResponse("Hello Tharun",content_type="text/plain")

def tharun1(request):
    return JsonResponse({"message":"Hello Tharun"})
