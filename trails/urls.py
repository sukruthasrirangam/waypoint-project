from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_catalog, name='trail_catalog'),
]