from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
# from rest_framework.decorators import action
# from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import OnlyAuthorPermission
from .models import CategoryPost, Post, Comment
from .serializer import PostListSerializer, CategorySerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
# from rest_framework import generics, mixins, views
# from django.core.exceptions import ObjectDoesNotExist


class BlogAPILIstPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):  # (mixins.ListModelMixin, viewsets.GenericViewSet)
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

    # @action(detail=True)
    # def detail_post(self, request, *args, **kwargs):
    #     post = self.get_object()
    #     serializer = PostDetailSerializer(post)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        # Устанавливаем автора поста как текущего пользователя
        serializer.save(author=self.request.user)


# class PostViewSet(viewsets.ModelViewSet):
#                    (mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    GenericViewSet):
#     queryset = Post.objects.all()  # Берем все записи из нужной табл в БД
#     serializer_class = PostSerializer  # подключаем DRF
#     lookup_field = 'slug'
#     permission_classes = [AllowAny, OnlyAuthorPermission]
#
#     def perform_create(self, serializer):
#         # Устанавливаем автора поста как текущего пользователя
#         serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryPost.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    # def dispatch(self, request, *args, **kwargs):
    #     try:
    #         response = super().dispatch(request, *args, **kwargs)
    #     except Exception as e:
    #         return self.response({'errorMessage': e.message}, status=400)
    #
    #     if isinstance(response, (dict, list)):
    #         return self.response(response)
    #     else:
    #         return response

    # def retrieve(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #     except ObjectDoesNotExist:
    #         return Response({"error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


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
