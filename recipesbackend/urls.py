
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', TokenObtainPairView.as_view(), name='api_auth'),
    path('api/auth/refresh', TokenRefreshView.as_view(), name='api_refresh'),
    path('api/', include(('recipes.urls', 'recipes'), namespace='recipes')),
]
