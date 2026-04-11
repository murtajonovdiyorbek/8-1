from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Car
from rest_framework.exceptions import NotFound

from .serializers import CategorySerializer, CarSerializer

class CategoryView(APIView):
    def get_c(self, request: Request, pk=None):
        if pk:
            category = Category.objects.filter(pk=pk).values().first()

            if not category:
                raise NotFound(detail="category topilmadi")

            return Response(category)


        category = Category.objects.values()
        return Response(category)

    def get(self, request: Request, pk=None):
        if pk:
            category = self.get_category(pk)

            serializer = CategorySerializer(category)

            return Response(serializer.data)

        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


    def post(self,request:Request):
        serializer = CategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message':"Malumotlar topildi"
        })

    def put(self,request:Request,pk):
        category = self.get_category(pk)

        serializer = CategorySerializer(instance=category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message':"Malumotlar yangilandi"
        })

    def patch(self,request:Request,pk):
        category = self.get_category(pk)

        serializer = CategorySerializer(instance=category,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message'"Ma'lumotlar yangilandi"
        })


    def delete(self, request: Request, pk):
        category = Category.objects.filter(pk=pk).first()

        if not category:
            raise NotFound(detail="category topilmadi")


        category.delete()

        return Response({
            "message": "category o'chirildi"
        })



class CarView(APIView):
    def get_c(self, request: Request, pk=None):
        if pk:
            car = Car.objects.filter(pk=pk).values().first()

            if not car:
                raise NotFound(detail="Car topilmadi")

            return Response(car)


        car = Car.objects.values()
        return Response(car)


    def get(self,request:Request,pk=None):
        if pk:
            car = self.get_car(pk)

            serializer = CarSerializer(car)

            return Response(serializer.data)

        cars = Car.objects.all()

        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)

    def post(self,request:Request):
        serializer = CarSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message':"Malumotlar topildi"
        })

    def put(self,request:Request,pk):
        car = self.get_car(pk)

        serializer = CarSerializer(instance=car,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message':"Malumotlar yangilandi"
        })

    def patch(self,request:Request,pk):
        car = self.get_car(pk)

        serializer = CarSerializer(instance=car,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message'"Ma'lumotlar yangilandi"
        })


    def delete(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="car topilmadi")


        car.delete()

        return Response({
            "message": "Car o'chirildi"
        })