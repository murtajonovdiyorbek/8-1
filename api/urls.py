from django.urls import path
from .views import  CarUpdateDestroyView, CarListCreateView, RegisterView

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='students'),
    path('cars/<int:pk>/', CarUpdateDestroyView.as_view(), name="update"),
    path('register/', RegisterView.as_view(), name="register")
    ]