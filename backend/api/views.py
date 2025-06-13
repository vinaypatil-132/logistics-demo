from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def trip_list(request):
    data = {
        "trips": [
            {"id": 1, "destination": "Bangalore", "driver": "Vinay"},
            {"id": 2, "destination": "Mumbai", "driver": "Ravi"}
        ]
    }
    return JsonResponse(data)

