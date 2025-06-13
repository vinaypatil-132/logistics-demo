from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Existing trip_list view
def trip_list(request):
    data = {
        "trips": [
            {"id": 1, "destination": "Bangalore", "driver": "Vinay"},
            {"id": 2, "destination": "Mumbai", "driver": "Ravi"}
        ]
    }
    return JsonResponse(data)

# New home view for "/"
def home(request):
    return HttpResponse("Welcome to the Logistics Demo Website!")
