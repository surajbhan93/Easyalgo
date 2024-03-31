from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import cs_subject

@admin.register(cs_subject)
class HtmlpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')  # Display these fields in the list view of the admin panel
    search_fields = ('title',)  # Add search functionality for the 'title' field
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
    # You can customize the admin interface further as needed


