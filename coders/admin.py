from django.contrib import admin
from .models import Pioneer, Member


class PioneerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'about')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name_mem', 'title_mem', 'about_mem')


admin.site.register(Pioneer, PioneerAdmin)
admin.site.register(Member, MemberAdmin)

