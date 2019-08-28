from django.conf.urls import url
from .views import index, faq

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^faq/$', faq, name="faq"),
    ]