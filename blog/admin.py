from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author","date","tag")
    list_display = ("title", "author","date")

admin.site.register(models.Author)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Tag)
# Register your models here.
