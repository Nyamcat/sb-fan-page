from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

# Create your models here.


class HashTag(models.Model):
    title = models.CharField(blank=True, null=True, max_length=50)
    nou = models.IntegerField(blank=True, null=True, default=1)


class Category(models.Model):
    title = models.CharField(blank=True, null=True, max_length=50)
    label = models.CharField(blank=True, null=True, max_length=50)
    nou = models.IntegerField(blank=True, null=True, default=1)


class SummerNote(summer_model.Attachment):
    title = models.CharField(blank=True, null=True, max_length=50)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    summer_field = summer_fields.SummernoteTextField(default='')
    hits = models.IntegerField(blank=True, null=True, default=0)
    noc = models.IntegerField(blank=True, null=True, default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    edited_date = models.DateTimeField(blank=True, null=True)
    hashtag = models.CharField(blank=True, null=True, max_length=500)
    tag1 = models.CharField(blank=True, null=True, max_length=50)
    tag2 = models.CharField(blank=True, null=True, max_length=50)
    tag3 = models.CharField(blank=True, null=True, max_length=50)
    tag4 = models.CharField(blank=True, null=True, max_length=50)
    tag5 = models.CharField(blank=True, null=True, max_length=50)


class Comment(models.Model):
    post = models.ForeignKey(SummerNote, models.DO_NOTHING, blank=True, null=True)
    ip = models.CharField(max_length=16, null=False, default='')
    comment = models.CharField(max_length=150, null=False, default='')
    author = models.CharField(max_length=9, null=False, default='')
    password = models.CharField(max_length=300, null=False, default='')
    depth = models.IntegerField(null=True)
    parent = models.IntegerField(null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    delete = models.CharField(max_length=2, default='N')
