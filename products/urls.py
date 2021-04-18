from django.urls import path
from .views import ProductListView, SingleProductRetrieveView, ProductListCreateView, ProductsRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', SingleProductRetrieveView.as_view()),
    path('edit_add_or_list/', ProductListCreateView.as_view()),
    path('edit_add_or_list/<int:pk>/', ProductsRetrieveUpdateDestroyView.as_view()),
]
