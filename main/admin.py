from django.contrib import admin

from .models import *

class PostImageInLine(admin.TabularInline):
    model = PostImage
    min_num = 1
    max_num = 15

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine, ]



admin.site.register(Category)

