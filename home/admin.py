from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def avatar(self, object):
        return format_html('<img src="{}" width="60" style="border-radius: 50px" />'.format(object.photo.url))

    list_display = ('id', 'avatar', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'avatar', 'first_name', 'last_name', 'designation')
    search_fields = ('first_name', 'last_name')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
