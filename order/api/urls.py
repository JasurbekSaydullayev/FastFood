from rest_framework import routers

from order.api.views import OrderViewSet, OrderDeliveryViewSet, OrderViewForCouriers

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

router_delivery_confirm = routers.DefaultRouter()
router_delivery_confirm.register('order-delivery-confirm', OrderDeliveryViewSet, basename='order-delivery-confirm')

order_view_for_couriers = routers.DefaultRouter()
order_view_for_couriers.register('orders-for-couriers', OrderViewForCouriers)

urlpatterns = router.urls
urlpatterns += router_delivery_confirm.urls
urlpatterns += order_view_for_couriers.urls
