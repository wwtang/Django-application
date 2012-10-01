from django.contrib import admin
from cms.models import Story, Category

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title','owner','status','modified')
    search_fileds = ('title','content')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','modified','owner','created')

admin.site.register(Story,StoryAdmin)



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('label',)}

admin.site.register(Category,CategoryAdmin)
