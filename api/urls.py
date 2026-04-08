from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_detail'),

    path('car/', CarView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarView.as_view(), name='car_detail'),
]