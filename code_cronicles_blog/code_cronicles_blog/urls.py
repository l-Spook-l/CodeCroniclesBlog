from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Application - blog
    path('api/v1/', include('blog.urls')),

    # djoser
    # auth/users/ - Registration
    # auth/jwt/create/ - Token creation
    # auth/users/me/ - User information retrieval
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
