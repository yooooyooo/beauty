"""admin configuration of novels."""
from django.contrib import admin

from boy.novels.models import Novel


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    """admin config of Novel model."""
    list_display = ('id', 'name', 'author', 'rank', 'comment', 'updated')
    search_fields = ('name', 'author')
    list_filter = ('rank', 'updated')
