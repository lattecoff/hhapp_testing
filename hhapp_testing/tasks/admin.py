from django.contrib import admin
from .models import Category, Refrigerator

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Refrigerator)
class RefrigeratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_compressor', 'no_frost', 'category')
    list_filter = ('name', 'amount_compressor', 'no_frost', 'category')
    search_fields = ('name', 'amount_compressor', 'no_frost', 'category')