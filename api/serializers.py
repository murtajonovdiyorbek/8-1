from rest_framework import serializers

from .models import Car, Category

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model','year',)
        read_only_fields = ('id',)


    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("ismni bosh harfi kattada bolishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Ism faqat harflardan tashkil topgan bolishi kerak")

        return value

    def validate_year(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Yil faqata sondan iborat bolishi kerak")

        return value



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        read_only_fields = ('id',)

    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Ismni bosh harfi katta bilan yozilishi kerak")

        if not value.isalpha():
            raise serializers.ValidationError("Ism faqat harflardan tashkil topgan bolishi kerak")

        return value