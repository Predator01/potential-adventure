from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('polls.urls', namespace='polls1')),
    # url(r'', include('polls2.urls', namespace='polls2')),
]
