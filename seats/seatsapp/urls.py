from django.urls import path
from . import views

urlpatterns = [
    path('api/layout', views.layout, name='layout'),
    path('api/flag', views.flag, name='flag'),
    path('api/seating', views.seating, name='seating'),
    path('list/', views.seating_view, name='seating_view'),
]
