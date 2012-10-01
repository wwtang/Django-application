from django.db import models

# Create your models here.
import datetime
from markdown import markdown
from django.contrib import admin
from django.db.models import permalink
from django.contrib.auth.models import User

VIEWABLE_STATUS = [3,4]
   
class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager,self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
    label = models.CharField(blank=True,max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.label

    

class Story(models.Model):

    STATUS_CHOICE = (
            (1, "Needs Edit"),
            (2, "Needs Approval"),
            (3, "Published"),
            (4, "Archived"),
            )
            
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(default=datetime.datetime.now)#
    modified = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(User)#
    markdown_content = models.TextField()#
    html_content = models.TextField(editable=False)
    status = models.IntegerField(choices=STATUS_CHOICE,default=1)#

    class Meta:# zhu yi daxie
        ordering = ['modified']
        verbose_name_plural = "stories"

    @permalink
    def get_absolute_url(self):
        return ("cms-story",(),{'slug':self.slug})##ji xia lai

    admin_objects = models.Manager()
    objects = ViewableManager()

   # def __unicode__(self):
   #     return self.title  
   #
    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()
       

