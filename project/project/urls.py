from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('user_auth.urls', namespace='user_auth')),
    url(r'^admin/', include(admin.site.urls)),
]
