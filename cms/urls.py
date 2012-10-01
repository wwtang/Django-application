from cms.models import Story, Category
from django.conf.urls.defaults import *

info_dict = {'queryset':Story.objects.all(), 'template_object_name':'story'}

# the first two url uses the generic view
urlpatterns = patterns('django.views.generic.list_detail',
        # display an individual story
        url(r'^(?P<slug>[-\w]+)/$','object_detail',info_dict,name="cms-story"),
        # list all the stories
        url(r'^$', 'object_list', info_dict, name="cms-home"),
        )

urlpatterns += patterns('cms.views',
        #display list by category
        url(r'^category/(?P<slug>[-\w]+)/$','category',name="cms-category"),
        # display list by matching search request
        url(r'^search$','search',name="cms-search"),
        )
