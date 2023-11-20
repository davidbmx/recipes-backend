from rest_framework import routers

from users.views import UserCreateRetrieveView

router = routers.DefaultRouter()

router.register(r'users', UserCreateRetrieveView)

urlpatterns = router.urls
