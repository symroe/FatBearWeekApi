from django.contrib import admin

from bears.models import Bear


class BearAdmin(admin.ModelAdmin):
    search_fields = ("bear_name",)
    list_display = ["bear_name", "bear_number"]
    list_filter = ["bear_gender", "bear_size"]
    readonly_fields = ("bear_uuid",)


admin.site.register(Bear, BearAdmin)
