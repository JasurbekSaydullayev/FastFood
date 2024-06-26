from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='users')

urlpatterns = router.urls
