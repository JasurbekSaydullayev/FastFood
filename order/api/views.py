from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializer import OrderSerializer
from ..models import Order
from .permissions import CustomerOrAdmin, WaitressOrAdmin, CanObjectAccess, IsAdmin, WaitressOrCourierOrAdmin, \
    CourierOrAdmin


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

    def get_permissions(self):
        return [IsAuthenticated(), WaitressOrCourierOrAdmin()]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status == "Qabul qilindi":
            if request.user.type == "Courier":
                return Response({"message": "Mahsulot tayyor bo'lishini kuting"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif request.user.type == "Waitress":
                order.status = "Ovqat tayyor"
                order.save()
                return Response({"message": "Ovqat tayyorligi tasdiqlandi"},
                                status=status.HTTP_200_OK)
        elif order.status == "Ovqat tayyor":
            if request.user.type == "Courier":
                order.status = "Buyurtma yetkazib beruvchiga berilgan"
                order.save()
                return Response({"message": "Buyurtmani olganingiz tasdiqlandi"},
                                status=status.HTTP_200_OK)
            elif request.user.type == "Waitress":
                return Response({"message": "Ushbu buyurtma yetkazib beruvchiga berilgan"},
                                status=status.HTTP_200_OK)
        elif order.status == "Buyurtma yetkazib beruvchiga berilgan":
            if request.user.type == "Courier":
                order.status = "Yetkazib berilgan"
                order.save()
                return Response({"message": "Buyurtma yetkazib berildi"},
                                status=status.HTTP_200_OK)
            elif request.user.type == "Waitress":
                return Response({"message": "Ushbu buyurtma yetkazib beruvchiga berilgan"},
                                status=status.HTTP_200_OK)
        return Response({"message": "Usbhu buyurtma allaqachon yetkazib berilgan"}, status=status.HTTP_200_OK)


class OrderViewForCouriers(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']

    def get_permissions(self):
        return [IsAuthenticated(), CourierOrAdmin()]

    def list(self, request, *args, **kwargs):
        orders = Order.objects.filter(status="Qabul qilindi").all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
