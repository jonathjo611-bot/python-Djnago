from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('artist/', include('artist.urls')),
    path('playlist/', include('playlist.urls')),
    path('podcast/', include('podcast.urls')),
]
