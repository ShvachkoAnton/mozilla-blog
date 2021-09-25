from django.contrib import admin
from .models import Post,Profile
class PostAdmin(admin.ModelAdmin):
    list_display=['title','text','slug']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Profile)