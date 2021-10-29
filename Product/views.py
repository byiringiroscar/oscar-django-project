from django.shortcuts import render
from django.http import HttpResponse
from .models import Commodity


# Create your views here.

def home(request):
    return render(request, 'html/home.html')


def produc(request):
    user = request.user
    user_data = Commodity.objects.all()
    unique_data = Commodity.objects.get(price=5000.0)

    context = {
        'name': user,
        'products': user_data,
        'uni_prod': unique_data
    }

    return render(request, 'html/dashboard.html', context)


def detail_view(request, pksa):
    product = Commodity.objects.get(id=pksa)

    context = {
        'commodity': product
    }
    return render(request, 'html/detail_page.html', context)
