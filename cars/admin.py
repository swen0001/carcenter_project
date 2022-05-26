from django.contrib import admin
from .models import Car
from django.utils.html import format_html
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from rangefilter.filters import DateTimeRangeFilter


class CarAdmin(admin.ModelAdmin):

    def CarImage(self, object):
        return format_html('<img src="{}" width="100" style="border-radius: 15px" />'.format(object.car_photo_1.url))

    list_display = ('id', 'CarImage', 'car_title', 'region', 'year', 'price', 'body_style', 'is_featured')
    list_display_links = ('id', 'CarImage', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city')
    list_filter = (
        ('region', ChoiceDropdownFilter),
        ('fuel_type', DropdownFilter),
        ('year', DropdownFilter),
        ('created_date', DateTimeRangeFilter),
        'brand',
        'color',
        )


admin.site.register(Car, CarAdmin)
