from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializer import OrderSerializer
from ..models import Order
from .permissions import CustomerOrAdmin, WaitressOrAdmin, CanObjectAccess, IsAdmin


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), CustomerOrAdmin()]
        elif self.action == 'list':
            return [IsAuthenticated(), WaitressOrAdmin()]
        elif self.action == 'retrieve':
            return [IsAuthenticated(), CanObjectAccess()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsAdmin()]


class OrderDeliveryViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['put']
    permission_classes = [IsAuthenticated(), ]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.delivered = True
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)






