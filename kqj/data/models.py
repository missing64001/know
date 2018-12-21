from django.db import models

# Create your models here.




class Label(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名',blank=True,null=True)
    pid = models.IntegerField(verbose_name='父标签id',blank=True,null=True)

    # label queue and content queue use one queue like 1,2,3|4,5,6
    queue = models.TextField(verbose_name='顺序') 
    grade = models.SmallIntegerField(verbose_name='等级',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)

class Content(models.Model):
    labels = models.ManyToManyField(Label,verbose_name='标签')
    name = models.CharField(max_length=50,verbose_name='名称',blank=True,null=True)
    text = models.TextField(verbose_name='内容')
    # attachment = models.FileField(upload_to='uploads/')
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)

class History(models.Model):
    label = models.ForeignKey(Label,verbose_name='标签')
    content = models.ForeignKey(Content,verbose_name='内容')
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)