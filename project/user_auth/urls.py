from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^worker/new$', views.worker_signup, name='worker_login'),
]
