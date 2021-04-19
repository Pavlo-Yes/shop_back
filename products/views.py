from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from products.models import ProductModel
from products.serializer import ProductSerializer


class ProductListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class SingleProductRetrieveView(RetrieveAPIView):
    pagination_class = [AllowAny]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

#     # Дістаємо продукти певного юзера
#     def get_queryset(self):
#         return ProductModel.objects.filter(user=self.request.user)
