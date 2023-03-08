from django.contrib import admin

# Register your models here.

from .models import Category, News , Counts

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at','updated_at','photos','is_bool')
    list_display_links=('title','content') #link qib beradi
    search_fields=('title','content') # search qo'shib beradi

admin.site.register(News,NewsAdmin)
admin.site.register(Category)

class CountAdmin(admin.ModelAdmin):
    list_display=('category','counts')
    list_display_links=('category','counts') #link qib beradi
    search_fields=('category','counts') # search qo'shib beradi

admin.site.register(Counts,CountAdmin)