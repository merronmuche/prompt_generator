from django.contrib import admin


from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'created_at', 'updated_at')
    search_fields = ('pdf_file',)
    readonly_fields = ('created_at', 'updated_at')

    # If you want to customize the form, you can add form = YourCustomForm

admin.site.register(Document, DocumentAdmin)

