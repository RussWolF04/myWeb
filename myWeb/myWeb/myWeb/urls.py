from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),  # Добавляем маршрут news/новости компании
    path('training/', include('training.urls')),  # маршрут training/обучение (курсы)
    path('accounts/', include('django.contrib.auth.urls')),  # маршрут для вторизации пользователей
    path('accounts/', include('accounts.urls')),  # маршрут accounts/регистрация пользователей
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
