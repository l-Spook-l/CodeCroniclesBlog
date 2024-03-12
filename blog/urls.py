from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet, CategoryViewSet, PostListByCategory, CommentViewSet


urlpatterns = format_suffix_patterns([
    path('posts/', PostViewSet.as_view({'get': 'list'})),
    path('post/<slug:slug>/', PostViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('post-create/', PostViewSet.as_view({'post': 'create'})),

    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('category-info/<slug:slug>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/<slug:category_slug>/', PostListByCategory.as_view({'get': 'list'})),

    path('comment/', CommentViewSet.as_view({'post': 'create'})),
    path('comment/<int:pk>/', CommentViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'})),
])
