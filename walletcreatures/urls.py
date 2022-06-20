
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/',include('mainapp.api.urls')),
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls',namespace="mainapp")),

]
