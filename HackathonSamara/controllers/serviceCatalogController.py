from django.shortcuts import render
from django.db.models import Q
from HackathonSamara.apps import Service
from HackathonSamara.apps.main.category import Category

def service_catalog(request):
    services = Service.objects.all()

    # Получение фильтров из запроса
    category_id = request.GET.get('category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    rating_min = request.GET.get('rating_min')
    search_query = request.GET.get('q')

    # Применение фильтров
    if category_id:
        services = services.filter(category_id=category_id)
    if price_min:
        services = services.filter(price__gte=price_min)
    if price_max:
        services = services.filter(price__lte=price_max)
    if rating_min:
        services = services.filter(rating__gte=rating_min)
    if search_query:
        services = services.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Передача данных в шаблон
    categories = Category.objects.all()
    return render(request, 'services/catalog.html', {'services': services, 'categories': categories})
