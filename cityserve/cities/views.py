from django.shortcuts import render
from .models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})
# Create your views here.
