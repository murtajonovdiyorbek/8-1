from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Car, Category

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(min_length=8, max_length=126)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():

            raise serializers.ValidationError("bu usernamedagi foydalanuvchi mavjud")
        return value


    def validate_email(self, value):
        if "@" not in value and "." not in value:
            raise serializers.ValidationError("email notogri")
        return value


    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError({
                "password": "Parollar bir biriga mos emas!"
            })
        return attrs


    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        return User.objects.create_user(**validated_data, password=password)

        User.objects.create()


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
        if not value:
            raise serializers.ValidationError("Yil faqata sondan iborat bolishi kerak")

        return value


class CarAdminSerializer(serializers.ModelSerializer):
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
        if not value:
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