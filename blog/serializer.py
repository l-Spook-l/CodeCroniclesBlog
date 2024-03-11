# сериализатор - конвертирование python-кода в json и наоборот
from rest_framework import serializers
from .models import CategoryPost, Post, PostPhoto, Comment


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"  # поля которые нужны клиенту


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = ('id', 'name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Comment
        fields = "__all__"  # если надо все поля
