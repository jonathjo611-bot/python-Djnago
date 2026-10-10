from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('movies/', include('movies.urls')),
    path('series/', include('series.urls')),
    path('watchlist/', include('watchlist.urls')),
]
