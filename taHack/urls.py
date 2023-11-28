from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paths.urls')),
    path('', include('users.urls', namespace='users')),
]

admin.site.index_title = "TaHack Administration"
admin.site.site_header = "TaHack: Career Path Finder"
admin.site.site_title = "TaHack"