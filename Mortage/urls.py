from django.conf.urls import include, url
from django.contrib import admin
from moratge_app import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^client', views.html_to_pdf_view,name='client')
]
