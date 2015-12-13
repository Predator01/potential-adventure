from django.conf.urls import include, url, patterns
from polls import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
]
