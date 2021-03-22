from django.contrib import admin

from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
   list_display = ('id','name', 'email','listing','realtor_name','purchase_date',)
   list_display_links = ('id','name') 
   search_fields = ('email','listing','name',)
   list_per_page = 25

admin.site.register(Contact, ContactAdmin)
