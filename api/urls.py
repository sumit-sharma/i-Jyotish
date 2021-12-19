from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import AstrologerList, AstrologerListDetail


schema_view = get_schema_view(
    openapi.Info(
        title="I-Jyotish",
        default_version='v1',
        description="I-Jyotish API documentation",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('category/', include('categories.urls')),

    # swagger and redoc documentation
    path('api.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('astrologer/', AstrologerList.as_view(), name='astrologers.list'),
    path('astrologer/<int:pk>/', AstrologerListDetail.as_view()),


]
