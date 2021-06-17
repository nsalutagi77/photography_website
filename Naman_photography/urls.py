from django.contrib import admin
from django.urls import path, include
from portfolio import urls, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('portfolio/', include('portfolio.urls')),
    path('gallery/', views.gallery, name = 'gallery'),
    path('shop/', views.shop, name = 'shop'),
    path('photo/<str:pk>', views.viewPhoto, name = 'photo'),
    path('add/', views.addPhoto, name = 'add'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
