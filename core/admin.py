from django.contrib import admin
from .models import HeroSlide, Advantage, ContactInfo, SupportTicket

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle')

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'active')
    list_editable = ('icon', 'order', 'active')
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'schedule')

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'status', 'created_at')
    list_filter = ('status', 'topic', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('status',)
    readonly_fields = ('user', 'name', 'email', 'topic', 'message', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('status',)
        }),
        ('Информация о заявителе', {
            'fields': ('user', 'name', 'email')
        }),
        ('Содержание заявки', {
            'fields': ('topic', 'message')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def has_add_permission(self, request):
        return False
