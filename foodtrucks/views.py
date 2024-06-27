
# Create your views here.


from django.shortcuts import render
from .models import FoodTruck
from django.db.models import Q


def index(request):
    return render(request, 'index.html')

# View function to find food trucks near given coordinates
def find_food_trucks(request):
    # Retrieve latitude and longitude from request parameters
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))

    # Query to find food trucks within range of the given coordinates
    food_trucks = FoodTruck.objects.filter(
        Q(latitude__range=(latitude - 0.01, latitude + 0.01)) &
        Q(longitude__range=(longitude - 0.01, longitude + 0.01))
    )[:5]

    # Prepare context data to pass to the results.html template
    context = {
        'food_trucks': food_trucks,
        'latitude': latitude,
        'longitude': longitude
    }

    return render(request, 'results.html', context)
