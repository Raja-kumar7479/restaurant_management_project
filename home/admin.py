from django.contrib import admin

# Register your models here.
from .models import MenuCategory
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    