from django.contrib import admin
from .models import Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_tags')

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    display_tags.short_description = 'Tags'

admin.site.register(Tag)
admin.site.register(Post)