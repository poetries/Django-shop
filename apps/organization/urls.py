# _*_ coding:utf-8 _*_
from django.conf.urls import url, include

from .views import OrgView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', )
]