from django.contrib import admin
from .models import Category, Refrigerator

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Refrigerator)
class RefrigeratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_frost', 'amount_compressor', 'category')
    list_filter = ('name', 'no_frost', 'amount_compressor', 'category')
    search_fields = ('name', 'no_frost', 'amount_compressor', 'category')