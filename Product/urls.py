from django.contrib import admin
from django.urls import path, include

from . import views

name = 'Product'

urlpatterns = [
    path('', views.home, name='home'),
    path('produc', views.produc, name='produc'),
    path('<int:pksa>/', views.detail_view, name='detail_view')

]

