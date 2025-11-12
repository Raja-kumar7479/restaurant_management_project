from django.urls import path
from .views import (
    MenuCategoryListCreateAPIView
    MenuCategoryRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("categories/",MenuCategoryListCreateAPIView.as_view(), name="category-lsit-create"),
    path("categories/<int:pk>/",MenuCategoryRetrieveUpdateDestroyAPIView.as_view(),name = "category-detail"),
]