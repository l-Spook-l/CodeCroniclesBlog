from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import CategoryPost, Post, PostPhoto
from .serializer import PostSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Берем все записи из нужной табл в БД
    serializer_class = PostSerializer  # подключаем DRF
    # filterset_class = ProductFilter  # фильтрации записей модели "Product" на основе параметров запроса
    # filter_backends = [DjangoFilterBackend]
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryPost.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
