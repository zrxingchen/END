from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from organization.models import CourseOrg,Teacher

class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    name = models.CharField("课程名",max_length=50)
    desc = models.CharField("课程描述",max_length=300,default='')
    detail = models.TextField("课程详情",default='')
    degree = models.CharField('难度',choices=DEGREE_CHOICES, max_length=2,default='')
    learn_times = models.IntegerField("学习时长(分钟数)",default=0)
    students = models.IntegerField("学习人数",default=0)
    fav_nums = models.IntegerField("收藏人数",default=0)
    image = models.ImageField("封面图",upload_to="courses/%Y/%m",max_length=100,default='')
    click_nums = models.IntegerField("点击数",default=0)
    add_time = models.DateTimeField("添加时间",default=datetime.now,)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE,verbose_name="所属的机构",null=True,blank=True)
    category = models.CharField("课程类别",max_length=20,default="")
    tag = models.CharField('课程标签',default='',max_length=10)
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',null=True,blank=True,on_delete=models.CASCADE)
    youneed_know = models.CharField('课程须知',max_length=300,default='')
    teacher_tell = models.CharField("可以学到什么",max_length=300,default='')


    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        return self.lesson_set.all().count()
    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField("章节名",max_length=100)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_vedio(self):
        return self.video_set.all()

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)



class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100)
    download = models.FileField("资源文件",upload_to="course/resource/%Y/%m",max_length=100)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name