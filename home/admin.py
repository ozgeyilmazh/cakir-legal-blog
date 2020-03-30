from django.contrib import admin
from .models import Makale
# Register your models here.

class MakaleAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'publishing_date', 'slug']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']
    
    class Meta:
        model = Makale


admin.site.register(Makale, MakaleAdmin)
