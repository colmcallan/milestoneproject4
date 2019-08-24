"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as home_urls
from accounts import urls as accounts_urls
from bug import urls as bug_urls
from ticket import urls as ticket_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from search import urls as search_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^bug/', include(bug_urls)),
    url(r'^ticket/', include(ticket_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^search/', include(search_urls)),
]

admin.site.site_header = "Project"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome"

from django.contrib.auth.models import Group
admin.site.unregister(Group)