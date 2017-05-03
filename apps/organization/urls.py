from django.conf.urls import url

from .views import OrgView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list')
]