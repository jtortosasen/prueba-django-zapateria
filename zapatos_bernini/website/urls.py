from django.urls import path, include
import rest_framework.permissions as permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


router = DefaultRouter()
router.register('Articles', views.ItemViewSet, basename='articles')


schema_view = get_schema_view(
    openapi.Info(
        title="Zapateria Bernini Articles API",
        default_version='v1.0.0',
        description="Artículos en stock de Zapatería Bernini",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
