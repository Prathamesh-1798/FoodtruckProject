
# Create your views here.
from django.shortcuts import render
from .models import FoodTruck
from django.db.models import Q


from django.shortcuts import render
from .models import FoodTruck
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def find_food_trucks(request):
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))

    food_trucks = FoodTruck.objects.filter(
        Q(latitude__range=(latitude - 0.01, latitude + 0.01)) &
        Q(longitude__range=(longitude - 0.01, longitude + 0.01))
    )[:5]

    context = {
        'food_trucks': food_trucks,
        'latitude': latitude,
        'longitude': longitude
    }

    return render(request, 'results.html', context)
