from django.contrib import admin

from .models import BookInfo,HeroInfo
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):

    '''列表页属性'''
    # list_display：显示字段
    list_display = ['pk', 'btitle', 'bpub_date']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['btitle']
    # search_fields：搜索字段
    search_fields = ['btitle']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 5

    '''添加、修改页属性'''
    # fields：属性的先后顺序
    # fields = ['bpub_date', 'btitle']
    # fieldsets：属性分组
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hname', 'hgender', 'hcontent', 'hbook']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
