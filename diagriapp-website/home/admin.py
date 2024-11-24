from django.contrib import admin
from .models import *

admin.site.site_header = "إدارة دي أغري"
admin.site.index_title = "إدارة دي أغري"

admin.site.register(Plant)
admin.site.register(Article)
admin.site.register(NewsItem)



class AboutCompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding new instances if one already exists
        if AboutCompany.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the only instance
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Redirect directly to the first instance if it exists
        obj = AboutCompany.objects.first()
        if obj:
            return super().change_view(request, str(obj.id), form_url, extra_context)
        return super().change_view(request, object_id, form_url, extra_context)

    # Customize how fields are displayed
    list_display = ('email', 'phone_number', 'link_to_app')  # Display key fields in the list view
    fields = ('summary', 'goals', 'mission', 'vision', 'email', 'phone_number', 'link_to_app')  # Control field order

    # Add search and filtering options if applicable
    search_fields = ('email', 'phone_number')
    list_filter = ('email',)

admin.site.register(AboutCompany, AboutCompanyAdmin)