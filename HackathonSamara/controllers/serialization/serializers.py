from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from HackathonSamara.apps.main.models import (
    Category, Company, Filter, FilterValue, Service, User, Review
)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'service', 'userId', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']  # Поля, которые нельзя изменять


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Пример обработки пароля (например, его хеширования)."""
        password = validated_data.pop('password')
        user = User(**validated_data)
        # Реализуйте хэширование пароля, если требуется (например, через Django's make_password)
        user.password = make_password(password)
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'contact_info', 'portfolio']
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )  # Ссылки на подкатегории

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'subcategories']
        read_only_fields = ['id']


class FilterSerializer(serializers.ModelSerializer):
    values = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )  # Ссылки на связанные FilterValue

    class Meta:
        model = Filter
        fields = ['id', 'name', 'filter_type', 'values']
        read_only_fields = ['id']


class FilterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterValue
        fields = ['id', 'filter', 'value']
        read_only_fields = ['id']


class ServiceSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )  # Ссылки на связанные отзывы

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'description', 'price', 'rating', 'reviews_count',
            'category', 'company', 'reviews'
        ]
        read_only_fields = ['id', 'rating', 'reviews_count']  # Эти поля вычисляемы
