from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pksa>/', views.detail_view, name='detail-view'),
]
