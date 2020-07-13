from django.contrib import admin

from . import models


class ParticipantInline(admin.TabularInline):
    model = models.Participant


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['contact_phone', 'ticket_type', 'confirmed']
    list_filter = [
        'ticket_type',
        'confirmed',
    ]
    search_fields = ['contact_phone']
    inlines = [
        ParticipantInline,
    ]
