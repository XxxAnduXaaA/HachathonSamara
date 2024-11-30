from django.urls import path
from HackathonSamara.api.v1.main.views import CategoryView, CompanyView, FilterView, FilterValueView, ServiceView, UserView, ReviewView

from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="API для HackathonSamara",
        default_version='v1',
        description="Документация для API HackathonSamara",
        contact=openapi.Contact(email="example@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    # Category URLs
    path('categories/', CategoryView.as_view(), name='list-categories'),
    path('category/<int:pk>/', CategoryView.as_view(), name='detail-category'),  # GET, PUT, DELETE для категории по ID

    # Company URLs
    path('companies/', CompanyView.as_view(), name='list-companies'),
    path('company/<int:pk>/', CompanyView.as_view(), name='detail-company'),  # GET, PUT, DELETE для компании по ID

    # Filter URLs
    path('filters/', FilterView.as_view(), name='list-filters'),
    path('filter/<int:pk>/', FilterView.as_view(), name='detail-filter'),  # GET, PUT, DELETE для фильтра по ID

    # FilterValue URLs
    path('filter-values/', FilterValueView.as_view(), name='list-filter-values'),
    path('filter-value/<int:pk>/', FilterValueView.as_view(), name='detail-filter-value'),  # GET, PUT, DELETE для значения фильтра по ID

    # Service URLs
    path('services/', ServiceView.as_view(), name='list-services'),
    path('service/<int:pk>/', ServiceView.as_view(), name='detail-service'),  # GET, PUT, DELETE для услуги по ID

    # User URLs
    path('users/', UserView.as_view(), name='list-users'),
    path('user/<int:pk>/', UserView.as_view(), name='detail-user'),  # GET, PUT, DELETE для пользователя по ID

    # Review URLs
    path('reviews/', ReviewView.as_view(), name='list-reviews'),
    path('review/<int:pk>/', ReviewView.as_view(), name='detail-review'),  # GET, PUT, DELETE для отзыва по ID
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
