from django.urls import path
from .views import trip_list, home

urlpatterns = [
    path('', home),             # This handles the root "/"
    path('trips/', trip_list),  # Existing trips endpoint
]
