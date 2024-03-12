# сериализатор - конвертирование python-кода в json и наоборот
from rest_framework import serializers
from .models import CategoryPost, Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # category = serializers.StringRelatedField(source='category.name', read_only=False)
    comments = CommentSerializer(many=True, read_only=True)  # related_name=comments в модели Comment

    class Meta:
        model = Post
        # exclude = ('content',)
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = ('id', 'name', 'slug')
