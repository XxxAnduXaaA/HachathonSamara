from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="subcategories", verbose_name="Родительская категория"
    )

class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание компании", blank=True)
    contact_info = models.TextField(verbose_name="Контактная информация", blank=True)
    portfolio = models.TextField(verbose_name="Портфолио", blank=True)

class Filter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название фильтра")
    filter_type = models.CharField(
        max_length=50,
        choices=(
            ("range", "Диапазон"),
            ("checkbox", "Чекбоксы"),
            ("dropdown", "Выпадающий список"),
        ),
        verbose_name="Тип фильтра"
    )

class FilterValue(models.Model):
    filter = models.ForeignKey(
        Filter, on_delete=models.CASCADE, related_name="values", verbose_name="Фильтр"
    )
    value = models.CharField(max_length=255, verbose_name="Значение фильтра")

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    rating = models.FloatField(verbose_name="Рейтинг", default=0)
    reviews_count = models.PositiveIntegerField(verbose_name="Количество отзывов", default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="services", verbose_name="Категория"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="services", verbose_name="Компания"
    )

class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Review(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="reviews", verbose_name="Услуга"
    )
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Имя пользователя"
    )
    rating = models.IntegerField(verbose_name="Оценка", choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")




