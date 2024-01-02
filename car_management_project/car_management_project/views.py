from django.shortcuts import render
from car_model.models import CarModel
from brand_model.models import BrandModel
from car_model.models import CarModel


# def home(request):
#     return render(request,'base.html')


def display_car(request, category_slug = None):
    carData = CarModel.objects.all()
    if category_slug is not None:
        find_car_model = BrandModel.objects.get(slug=category_slug)
        carData = CarModel.objects.filter(car_model = find_car_model)
    category_model = BrandModel.objects.all()
    return render(request,'display_car.html', {'carData': carData,'modelCategoryData': category_model})