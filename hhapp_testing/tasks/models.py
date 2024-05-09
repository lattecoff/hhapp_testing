from django.db import models

# Create your models here.
class Category(models.Model):
    DEV_CATEGORY = (
        ('refrigerator', 'Refrigerator'),
        ('washing_mach', 'Washing Machine')
    )

    id_cat = models.PositiveIntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=50, choices=DEV_CATEGORY, db_index=True, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name',]


class Refrigerator(models.Model):
    id_ref = models.PositiveIntegerField(primary_key=True, serialize=True)
    name = models.CharField(verbose_name='Name', max_length=100, blank=False)
    amount_compressor = models.PositiveSmallIntegerField(blank=False)
    no_frost = models.BooleanField(blank=False, default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Refrigerator'
        verbose_name_plural = 'Refrigerators'
        ordering = ['name', 'amount_compressor', 'category']