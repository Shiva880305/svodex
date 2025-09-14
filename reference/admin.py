# reference/admin.py
from django.contrib import admin
from .models import Reference, ReferenceImage, Service, ServiceImage, Certificate, Stat # Přidán ServiceImage
from django.utils.html import format_html


class ReferenceImageInline(admin.TabularInline):
    model = ReferenceImage
    extra = 1

class ServiceImageInline(admin.StackedInline):
    model = ServiceImage
    extra = 1 # Počet prázdných formulářů pro obrázky

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_added')
    search_fields = ('title', 'description')
    inlines = [ReferenceImageInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]
    list_display = ('title', 'icon')
    search_fields = ('title',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issue_date', 'certificate_file')
    search_fields = ('name',)

    def certificate_file(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Stáhnout</a>', obj.file.url)
        return 'Žádný soubor'

    certificate_file.short_description = 'Soubor'


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'description')
    search_fields = ('title', 'description')


# Přizpůsobení administrace
admin.site.site_header = format_html('<img src="/static/img/logo_wh.png" alt="Svodex Logo" style="height:40px;">')
admin.site.site_title = "Svodex"
admin.site.index_title = "Správa webu"