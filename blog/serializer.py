from rest_framework import serializers
from .models import CategoryPost, Post, PostPhoto


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = ('id', 'name', 'slug')



