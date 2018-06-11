from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']

    class Media:
        js = [
            '/static/blog/js/jquery-2.1.3.min.js',   # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textareas.js',   # 手动添加文件，用户初始化参数
        ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)