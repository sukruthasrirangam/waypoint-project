from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_catalog, name='trail_catalog'),
    path('park/<int:park_id>/', views.trails_by_park, name='trails_by_park'),
    path('<int:trail_id>/', views.trail_detail, name='trail_detail'),
]