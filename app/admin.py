from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Contact
from import_export.admin import ImportExportModelAdmin
 
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'gender', 'info') 
    list_display_links = ('id', 'name')
    list_filter = ('gender','date')
    list_per_page = 10
    list_editable = ('info',)
    search_fields = ('name', 'email', 'phone', 'gender')



admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)

