from .models import Post
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__slug', lookup_expr='in')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    ordering = filters.OrderingFilter(fields=["time_create"])

    class Meta:
        model = Post
        fields = ['category', 'title']
