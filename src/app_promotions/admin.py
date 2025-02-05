from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)