from django.contrib import admin
from .models import Jewelry, JewelryInstance, Size, Accessories, Forma, Status, Stone
from django.utils.html import format_html


class JewelryInstanceInline(admin.TabularInline):
    model = JewelryInstance


# admin.site.register(Jewelry)
@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('name', 'forma', 'display_stone', 'price', 'show_photo')
    list_filter = ('forma', 'stone')
    inlines = [JewelryInstanceInline]
    readonly_fields = ["show_photo"]

    def show_photo(self,obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">')
    show_photo.short_description = 'Фото'




# admin.site.register(JewelryInstance)
@admin.register(JewelryInstance)
class JewelryInstanceAdmin(admin.ModelAdmin):
    list_filter = ('jewelry', 'status')
    fieldsets = (
        ('Экземпляр украшения', {
            'fields': ('jewelry', 'inv_num')}),
        ('Статус и окончание его действия',{
            'fields': ('status', 'due_back')
        })
    )



admin.site.register(Size)
admin.site.register(Accessories)
admin.site.register(Forma)
admin.site.register(Status)


class StoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'show_photo')
    readonly_fields = ["show_photo"]

    def show_photo(self,obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">'
        )
    show_photo.short_description = 'Фото'


admin.site.register(Stone, StoneAdmin)
