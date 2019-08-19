from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','context','created_at','update_at')


admin.site.register(Article, ArticleAdmin)