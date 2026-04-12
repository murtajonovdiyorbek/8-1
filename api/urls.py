from django.urls import path
from .views import  CarListCreateView, CarDetailUpdateDeleteAPIView

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='students'),
    path('cars/<int:pk>/', CarDetailUpdateDeleteAPIView.as_view(), name="update"),
    ]