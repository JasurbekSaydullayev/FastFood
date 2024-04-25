from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsWaitressOrAdmin
from .serializers import FoodSerializer
from foods.models import Food


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        else:
            return [IsAuthenticated(), IsWaitressOrAdmin()]
