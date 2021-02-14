from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "KM Admin"
admin.site.site_title = "KM Admin Portal"
admin.site.index_title = "Welcome to KM Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
