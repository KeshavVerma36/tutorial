from django.contrib import admin
from .models import Articles
# Register your models here.
class Articleadmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title", "content"]

admin.site.register(Articles, Articleadmin)