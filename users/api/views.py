from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.api.serializer import UserSerializer
from users.models import User
from users.permissions import CanAccessObject, IsStaff
from users.validators import check_phone_number
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'list':
            return [IsStaff()]
        return [CanAccessObject()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if not check_phone_number(serializer.validated_data['phone_number']):
                return Response({"message": "Invalid phone number"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
