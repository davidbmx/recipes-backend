
from django.contrib import admin
from django.urls import path, include
from users.views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', CustomTokenObtainPairView.as_view(), name='api_auth'),
    path('api/auth/refresh', TokenRefreshView.as_view(), name='api_refresh'),
    path('api/', include(('recipes.urls', 'recipes'), namespace='recipes')),
    path('api/', include(('users.urls', 'users'), namespace='users')),
]
