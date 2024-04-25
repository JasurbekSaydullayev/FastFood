from rest_framework import routers

from order.api.views import OrderViewSet, OrderDeliveryViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

router_delivery_confirm = routers.DefaultRouter()
router_delivery_confirm.register('order-delivery-confirm', OrderDeliveryViewSet, basename='order-delivery-confirm')

urlpatterns = router.urls
urlpatterns += router_delivery_confirm.urls
