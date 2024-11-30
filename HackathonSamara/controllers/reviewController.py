from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from HackathonSamara.apps.main.review import Review
from .serialization.reviewSerialization import ReviewSerializer

# Список отзывов и добавление нового
class ReviewController(APIView):
    def get(self, request):
        querySet = Review.objects.all()
        serializerForQuerySet = ReviewSerializer(instance=querySet, many=True)

        return Response(serializerForQuerySet.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)

        # if request.user.is_authenticated:
        serializer.validated_data['user'] = request.user

        # Проверяем валидность данных
        if serializer.is_valid():
            serializer.save()  # Сохраняем данные в базе
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Если данные не валидны, возвращаем ошибки
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
