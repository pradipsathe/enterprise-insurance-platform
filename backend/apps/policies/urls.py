from django.urls import path
from .views import (
    PolicyListAPIView,
    PolicyCreateAPIView,
    PolicyUpdateAPIView,
    PolicyDeleteAPIView,
)

urlpatterns = [
    path("", PolicyListAPIView.as_view()),
    path("create/", PolicyCreateAPIView.as_view()),
    path("<uuid:pk>/update/", PolicyUpdateAPIView.as_view()),
    path("<uuid:pk>/delete/", PolicyDeleteAPIView.as_view()),
]