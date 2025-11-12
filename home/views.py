from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from.models import MenuCategory
from.serializers import MenuCategorySerializers
class MenuCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class =MenuCategorySerializers
class MenuCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializers
