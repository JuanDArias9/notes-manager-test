from django.contrib import admin

from notes.models import Note

@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")
    list_filter = ("category",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
