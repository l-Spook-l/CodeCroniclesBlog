from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import CategoryPost, Post, PostPhoto
from .serializer import PostSerializer, CategorySerializer


class PostAPILIstPagination(PageNumberPagination):
    page_size = 3  # кол-во записей на 1й стр
    page_query_param = 'page'
    max_page_size = 1000  # Ограничение записей на 1й стр для - page_query_param = 'page_size'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Берем все записи из нужной табл в БД
    serializer_class = PostSerializer  # подключаем DRF
    # filterset_class = ProductFilter  # фильтрации записей модели "Product" на основе параметров запроса
    # filter_backends = [DjangoFilterBackend]
    pagination_class = PostAPILIstPagination  # Пагинация
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryPost.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PostListByCategory(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    # filterset_class = CategoryFilter
    # filter_backends = [DjangoFilterBackend]
    pagination_class = PostAPILIstPagination

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(CategoryPost, slug=category_slug)
        queryset = Post.objects.filter(category=category)
        return queryset
