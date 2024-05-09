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
        ordering = ['name', 'amount_compressor', 'no_frost', 'category']


class ResearchRef(models.Model):
    RES_STATUS = (
        ('success', 'Success'),
        ('fail', 'Fail'),
        ('in_process', 'In Process')
    )

    id_res = models.PositiveIntegerField(primary_key=True, serialize=True)
    device = models.ForeignKey('Refrigerator', on_delete=models.PROTECT, null=True)
    describe = models.TextField(blank=True, null=True,  help_text='Additional info about research')
    status = models.CharField(max_length=50, choices=RES_STATUS, db_index=True, blank=False)
    date_start = models.DateField()
    date_finish = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Refrigerator research'
        verbose_name_plural = 'Refrigerator research'
        ordering = ['id_res', 'device', 'status', 'date_start', 'date_finish']
