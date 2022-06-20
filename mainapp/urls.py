from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mainapp import views
app_name = 'mainapp'

urlpatterns = [
    path('', views.SearchView.as_view(), name="template"),

]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
