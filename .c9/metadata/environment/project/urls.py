{"filter":false,"title":"urls.py","tooltip":"/project/urls.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":15,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]",""],"id":2},{"start":{"row":15,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from checkout import urls as urls_checkout","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}],[{"start":{"row":0,"column":0},"end":{"row":35,"column":1},"action":"remove","lines":["\"\"\"project URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from checkout import urls as urls_checkout","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"],"id":5},{"start":{"row":0,"column":0},"end":{"row":41,"column":28},"action":"insert","lines":["\"\"\"unicornattractor URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url, include","from django.contrib import admin","from home import urls as home_urls","from accounts import urls as accounts_urls","from bugs import urls as bugs_urls","from features import urls as features_urls","from cart import urls as cart_urls","from checkout import urls as checkout_urls","from search import urls as search_urls","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^', include(home_urls)),","    url(r'^accounts/', include(accounts_urls)),","    url(r'^bugs/', include(bugs_urls)),","    url(r'^features/', include(features_urls)),","    url(r'^cart/', include(cart_urls)),","    url(r'^checkout/', include(checkout_urls)),","    url(r'^search/', include(search_urls)),","]","","","admin.site.site_header = \"Unicorn Attractor\"","admin.site.site_title = \"Admin Area\"","admin.site.index_title = \"Welcome\"","","from django.contrib.auth.models import Group","admin.site.unregister(Group)"]}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"remove","lines":["r"],"id":6},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"remove","lines":["o"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"remove","lines":["t"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"remove","lines":["c"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"remove","lines":["a"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"remove","lines":["r"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"remove","lines":["t"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"remove","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"remove","lines":["a"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["n"]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":["r"],"id":7},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["o"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":["c"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["i"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["n"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["u"]}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["I"],"id":8},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["s"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["s"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["u"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["r"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":["e"],"id":9},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["r"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["e"],"id":10}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":[" "],"id":11},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["T"]}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["T"],"id":12}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["B"],"id":13},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["u"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["g"]}],[{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":[" "],"id":14},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["T"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["r"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["a"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["c"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["k"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["e"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"remove","lines":["r"],"id":15},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"remove","lines":["e"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"remove","lines":["k"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"remove","lines":["c"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"remove","lines":["a"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"remove","lines":["r"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"remove","lines":["T"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"remove","lines":[" "]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"remove","lines":["g"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"remove","lines":["u"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["B"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":[" "]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["e"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":["u"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["s"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["s"]}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["I"],"id":16}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["p"],"id":17},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["o"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["j"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["e"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["c"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":36,"column":41},"end":{"row":36,"column":42},"action":"remove","lines":["o"],"id":18},{"start":{"row":36,"column":40},"end":{"row":36,"column":41},"action":"remove","lines":["t"]},{"start":{"row":36,"column":39},"end":{"row":36,"column":40},"action":"remove","lines":["c"]},{"start":{"row":36,"column":38},"end":{"row":36,"column":39},"action":"remove","lines":["a"]},{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"remove","lines":["r"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"remove","lines":["t"]},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"remove","lines":["t"]},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"remove","lines":["A"]},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"remove","lines":[" "]},{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"remove","lines":["n"]},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"remove","lines":["r"]}],[{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"remove","lines":["o"],"id":19},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"remove","lines":["c"]},{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"remove","lines":["i"]},{"start":{"row":36,"column":27},"end":{"row":36,"column":28},"action":"remove","lines":["n"]},{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"remove","lines":["U"]}],[{"start":{"row":37,"column":25},"end":{"row":37,"column":35},"action":"remove","lines":["Admin Area"],"id":20}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"remove","lines":["e"],"id":21},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"remove","lines":["m"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"remove","lines":["o"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"remove","lines":["c"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"remove","lines":["l"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"remove","lines":["e"]}],[{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"remove","lines":["r"],"id":22}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":36,"column":26},"end":{"row":36,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566350232870,"hash":"0361e139d14360c66513ae671bbaf70a954688bf"}