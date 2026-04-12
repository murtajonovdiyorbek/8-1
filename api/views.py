from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Car
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


from .serializers import CategorySerializer, CarSerializer, CarAdminSerializer

class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CarAdminSerializer
        else:
            return CarSerializer

class CarDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def get_object(self):
        car = self.queryset.get(pk=self.kwargs['pk'])
        return car


class CategoryListCreateView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()