from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from HackathonSamara.apps import User
from .serialization.userSerialization import UserSerializer
# Список отзывов и добавление нового
class UserController(APIView):
    def get(self, request):
        query = User.objects.get(id=request.user.id)
        serializerForQuery = UserSerializer(instance=query)

        return Response(serializerForQuery.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        # Проверяем валидность данных
        if serializer.is_valid():
            user = serializer.save()  # Сохраняем данные в базе
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            # Если данные не валидны, возвращаем ошибки
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
