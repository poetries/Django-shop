# _*_ coding _*_

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse

# 添加课程的时候可以顺便添加章节
class LessonInline:
    model = Lesson
    extra = 0


# 添加课程的时候可以顺便添加课程资源
class CourseResourceInline:
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    model_icon = 'fa fa-graduation-cap'

    # Inline # 添加课程的时候可以顺便添加章节、课程资源
    inlines = [LessonInline, CourseResourceInline]

    # 重新在这里写一遍的原因是，避免数据重复
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']



    #Inline # 添加课程的时候可以顺便添加章节、课程资源
    inlines = [LessonInline, CourseResourceInline]

    #把轮播图从 User model 里转移到 Course model 里
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'download', 'name']
    list_filter = ['course__name', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
