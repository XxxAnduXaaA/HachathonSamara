from rest_framework import serializers
from HackathonSamara.apps.main.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'service', 'user_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user_name', 'created_at']

        # Вы можете исключить поле user, если оно не передается в запросе
        def create(self, validated_data):
            # Привязываем пользователя в методе создания
            user = self.context['request'].user  # Получаем текущего пользователя из запроса
            validated_data['user'] = user
            return super().create(validated_data)