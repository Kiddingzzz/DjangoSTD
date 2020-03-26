from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
# add by chr 20160719
from django.utils.html import format_html


class 教师审核(models.Model):
    shenheStatu = models.CharField(max_length=50, default='',verbose_name = '审核状态')
    teacherid = models.CharField(max_length=50, default='',verbose_name = '老师编号')
    teachername = models.CharField(max_length=50, default='',verbose_name = '老师姓名')
INSTALLED_APPS = (
    '教师审核',
)