from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm




@admin.register(About)
class AboutAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('address', 'email', 'phone', 'whatsapp', 'updated_at')
    fieldsets = (
        ("Basic Information", {
            "fields": ("address", "email", "phone", "whatsapp", "location"),
        }),
        ("Visibility Settings", {
            "fields": ("show_address", "show_email", "show_phone", "show_whatsapp", "show_location"),
        }),
    )

    import_form_class = ImportForm
    export_form_class = ExportForm
    # list_filter = ["name", "code", "updated_at"]










# @admin.register(Currency)
class CurrencyAdmin(ModelAdmin, ImportExportModelAdmin):
    # Fields to display in the admin panel list view
    list_display = ('order', 'code', 'name', 'buy_rate', 'sell_rate', 'is_active', 'hidden_status', 'updated_at')

    # Make the 'code' field clickable as a link
    list_display_links = ('code',)

    # Fields that can be edited directly in the list view
    list_editable = ('order', 'is_active')  # Allow editing the 'order' and 'is_active' fields

    # Default ordering of rows in the admin panel
    ordering = ('order',)

    import_form_class = ImportForm
    export_form_class = ExportForm
    list_filter = ["name", "code", "updated_at"]


# @admin.register(Configuration)
class ConfigurationAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('prices_fee', 'show_prices_fee', 'updated_at')
    list_editable = ('show_prices_fee',)

    import_form_class = ImportForm
    export_form_class = ExportForm
    list_filter = ["prices_fee", "updated_at"]