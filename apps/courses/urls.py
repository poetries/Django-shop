# _*_ coding:utf-8 _*_
from django.conf.urls import url, include

from .views import CourseListView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
]