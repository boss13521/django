from django.contrib import admin
from models import *

class HeroInfoline(admin.StackedInline):
    model = HeroInfo
    extra = 2



class BookInfoAdmin(admin.ModelAdmin):

    list_display = ['id','btitle','bpub_date']

    list_filter = ['btitle']

    search_fields = ['btitle']

    list_per_page = 10

    fieldsets = [

        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']}),
    ]

    inlines = [HeroInfoline]



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)

