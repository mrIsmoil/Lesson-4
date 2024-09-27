from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
from rest_framework_simplejwt.views import ( # type: ignore
   TokenObtainPairView,
   TokenRefreshView
)



schema_view = get_schema_view(
   openapi.Info(
      title="Car Shop",
      default_version='v1',
      description="You can find very luxury cars with us",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzQ0ODQ5NSwiaWF0IjoxNzI3MzYyMDk1LCJqdGkiOiI2YzhhZmM0MjIwNzc0ZWQxYmMwZTk5MDUwYzljNGRlMyIsInVzZXJfaWQiOjJ9.1WGBHvXwhHsiubPZ_nqGqqIErqtQNftz31aPMhOwhMw"