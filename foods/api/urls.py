from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('foods', FoodViewSet, basename='foods')

urlpatterns = router.urls
