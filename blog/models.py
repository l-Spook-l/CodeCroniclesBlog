from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# from django.contrib.auth import models as auth_models


# class User(auth_models.AbstractUser):
#     """Моя модель для пользователя"""
#     first_name = models.CharField(verbose_name="First name", max_length=255)
#     last_name = models.CharField(verbose_name="Last name", max_length=255)
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def __str__(self):
#         return self.first_name


class CategoryPost(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    # 'For the correct display of the title in the admin panel.'
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     # category - название в URL (name='category')
    #     return reverse('category', kwargs={'category_slug': self.slug})


class PostPhoto(models.Model):
    image = models.ImageField(upload_to='photos/post')

    def __str__(self):
        return self.image.name

    # для настройки в админ-панели
    class Meta:
        verbose_name = 'Post photo.'
        verbose_name_plural = 'Post photos'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photos = models.ManyToManyField(PostPhoto, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryPost, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # "Auto-generation of slug."
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    # "When deleting a product, delete the photos from the folder."
    def delete(self, *args, **kwargs):
        # "Delete the file associated with this record."
        self.photos.delete()
        super().delete(*args, **kwargs)

    # для настройки в админ-панели
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['title', 'time_create']  # сортировка везде
    #     ordering = ['time_create', 'price', '-price']  # сортировка везде


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        ordering = ['created_at']

