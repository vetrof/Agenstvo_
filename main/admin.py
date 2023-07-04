from django.contrib import admin

from main.models import Realty, Category, Manager, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'realty'
    model = Gallery


class RealtyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'cat', 'person')
    search_fields = ('title', 'info')
    ordering = ('-id',)
    inlines = [GalleryInline, ]


admin.site.register(Realty, RealtyAdmin)
admin.site.register(Category)
admin.site.register(Manager)
admin.site.register(Gallery)
