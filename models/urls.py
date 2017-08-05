from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^allstatus/$', views.status, name='status'),
    url(r'^poststatus/$', views.post_status, name='post_status'),
    url(r'^status/(?P<pk>\d+)/$', views.status_detail, name='status_detail'),
    url(r'^postnestedcomment/$', views.nestedcomment, name="nestedcomment"),
]