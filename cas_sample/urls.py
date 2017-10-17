from django.conf.urls import url
from . import views
import cas

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', 'cas.views.login', name='cas_ng_login'),
    url(r'^logout$', 'cas.views.logout', name='cas_ng_logout'),
]
