from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Car
from rest_framework.exceptions import NotFound



class CategoryView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            category = Category.objects.filter(pk=pk).values().first()

            if not category:
                raise NotFound(detail="category topilmadi")

            return Response(category)


        category = Category.objects.values()
        return Response(category)


    def post(self, request: Request):
        body = request.data

        Category.objects.create(**body)

        return Response({
            "message": "Ma'lumotlar saqlandi"
        })


    def put(self, request: Request, pk):
        category = Category.objects.filter(pk=pk).first()

        if not category:
            raise NotFound(detail="category topilmadi")


        body = request.data
        category.name = body.get('name', category.name)
        category.description = body.get('description', category.description)
        category.save()

        return Response({
            "message": "Malumotlar yangilandi"
        })


    def patch(self, request, pk):
        category = Category.objects.filter(pk=pk).first()

        if not category:
            raise NotFound(detail="category topilmadi")

        body = request.data
        category.name = body.get('name', category.name)
        category.description = body.get('description', category.description)

        category.save()

        return Response({
            "message": "Malumotlar yangilandi"
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
    def get(self, request: Request, pk=None):
        if pk:
            car = Car.objects.filter(pk=pk).values().first()

            if not car:
                raise NotFound(detail="Car topilmadi")

            return Response(car)


        car = Car.objects.values()
        return Response(car)


    def post(self, request: Request):
        body = request.data

        Car.objects.create(**body)

        return Response({
            "message": "Ma'lumotlar saqlandi"
        })


    def put(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="Car topilmadi")


        body = request.data
        car.brand = body.get('brand', car.brand)
        car.model = body.get('model', car.model)
        car.year = body.get('year', car.year)
        car.color = body.get('color', car.color)
        car.price = body.get('price', car.price)
        car.mileage = body.get('mileage', car.mileage)
        car.description = body.get('description', car.description)
        car.image = body.get('image', car.image)
        car.save()

        return Response({
            "message": "Malumotlar yangilandi"
        })


    def patch(self, request, pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="Car topilmadi")

        body = request.data
        car.brand = body.get('brand', car.brand)
        car.model = body.get('model', car.model)
        car.year = body.get('year', car.year)
        car.color = body.get('color', car.color)
        car.price = body.get('price', car.price)
        car.mileage = body.get('mileage', car.mileage)
        car.description = body.get('description', car.description)
        car.image = body.get('image', car.image)
        car.save()

        return Response({
            "message": "Malumotlar yangilandi"
        })


    def delete(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="car topilmadi")


        car.delete()

        return Response({
            "message": "Car o'chirildi"
        })