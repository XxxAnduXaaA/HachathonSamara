from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from HackathonSamara.controllers.serialization.serializers import *


# Общая базовая структура контроллеров
class BaseAPIView(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object(pk)
            if instance:
                serializer = self.serializer_class(instance)
                return Response(serializer.data)
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            instances = self.model.objects.all()
            serializer = self.serializer_class(instances, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CategorySerializer)
    def put(self, request, pk):
        instance = self.get_object(pk)
        if not instance:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        if not instance:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Конкретные контроллеры для моделей
class CategoryView(BaseAPIView):
    model = Category
    serializer_class = CategorySerializer

    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=CategorySerializer)
    def put(self, request, pk):
        return super().put(request)


class CompanyView(BaseAPIView):
    model = Company
    serializer_class = CompanySerializer

    @swagger_auto_schema(request_body=CompanySerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=CompanySerializer)
    def put(self, request, pk):
        return super().put(request)


class FilterView(BaseAPIView):
    model = Filter
    serializer_class = FilterSerializer

    @swagger_auto_schema(request_body=FilterSerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=FilterSerializer)
    def put(self, request, pk):
        return super().put(request)


class FilterValueView(BaseAPIView):
    model = FilterValue
    serializer_class = FilterValueSerializer

    @swagger_auto_schema(request_body=FilterValueSerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=FilterValueSerializer)
    def put(self, request, pk):
        return super().put(request)


class ServiceView(BaseAPIView):
    model = Service
    serializer_class = ServiceSerializer

    @swagger_auto_schema(request_body=ServiceSerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=ServiceSerializer)
    def put(self, request, pk):
        return super().put(request)


class UserView(BaseAPIView):
    model = User
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request, pk):
        return super().put(request)


class ReviewView(BaseAPIView):
    model = Review
    serializer_class = ReviewSerializer

    @swagger_auto_schema(request_body=ReviewSerializer)
    def post(self, request):
        return super().post(request)

    @swagger_auto_schema(request_body=ReviewSerializer)
    def put(self, request, pk):
        return super().put(request)