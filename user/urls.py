from django.urls import path

from .views import UserListCreateView, GetCurrentUserView, SingleUserRetrieveView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('current/', GetCurrentUserView.as_view()),
    path('<int:pk>/', SingleUserRetrieveView.as_view())
]
