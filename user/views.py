from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import UserModel
from .serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

    # Виключення себе зі списку усіх зареєстрованих юзерів
    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(id=self.request.user.id)
        return Response(UserSerializer(qs, many=True).data)


class GetCurrentUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        data = UserSerializer(user).data
        return Response(data)


class SingleUserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
