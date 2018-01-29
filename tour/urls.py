from django.conf.urls import url
from . import views

app_name= 'tour'

urlpatterns = [
    #/home/
    url(r'^$', views.home, name='home'),

    #/home/new/
    url(r'^new/$',views.index,name='index'),

    #/home/1
    url(r'^(?P<trip_id>[0-9]+)/$',views.detail,name='detail'),

]
