from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^bill/',views.cal_amount,name='cal_amount'),
]
