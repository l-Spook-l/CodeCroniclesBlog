from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .permissions import OnlyAuthorPermission
from .models import CategoryPost, Post, Comment
from .serializer import PostListSerializer, CategorySerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter


class BlogAPILIstPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = BlogAPILIstPagination
    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ('partial_update', 'destroy'):
            permission_classes = [OnlyAuthorPermission]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryPost.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PostListByCategory(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostListSerializer
    pagination_class = BlogAPILIstPagination

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(CategoryPost, slug=category_slug)
        queryset = Post.objects.filter(category=category)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ('partial_update', 'destroy'):
            permission_classes = [OnlyAuthorPermission]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
