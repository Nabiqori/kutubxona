from django.contrib import admin

from .models import *
class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1

class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id", "ism","davlat","kitob_soni","tirik"]
    list_display_links = ["davlat","ism","id"]
    list_filter = ["davlat","tirik"]
    search_fields = ['ism']
    list_editable = ['kitob_soni', 'tirik']
    inlines = [KitobInline]

class KitobAdmin(admin.ModelAdmin):
    list_display = ["nom","muallif","sahifa","id"]
    list_display_links = ["nom","muallif","id"]
    list_filter = ["muallif","janr"]
    list_per_page = 10
    list_editable = ["sahifa"]
    search_fields = ["nom","janr"]
    search_help_text = "kitob nomi yoki janrni kiriting"
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["ism","ish_vaqti"]
    search_fields = ["ism"]
    list_filter = ["ish_vaqti"]
class RecordAdmin(admin.ModelAdmin):
    list_display = ["talaba__ism","kutubxonachi__ism","kitob__nom"]
    search_fields = ["talaba__ism","kutubxonachi__ism","kitob__nom"]
admin.site.register(Kitob,KitobAdmin)
admin.site.register(Record,RecordAdmin)
admin.site.register(Muallif,MuallifAdmin)
admin.site.register(Kutubxonachi,KutubxonachiAdmin)
