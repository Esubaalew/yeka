from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Author, Department, Research


# Register your models here.
class AuthorAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'get_researches')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)
    ordering = ('first_name', 'last_name')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email')
        }),
    )

    # Custom method to display researches related to the author
    def get_researches(self, obj):
        return ", ".join([research.title for research in obj.researches.all()])

    get_researches.short_description = 'Researches'


class DepartmentAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


class ResearchAdmin(ModelAdmin):
    list_display = ('title', 'department', 'file')
    search_fields = ('title', 'summary')
    list_filter = ('department',)
    ordering = ('title', 'department')
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'department', 'authors', 'file')
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Research, ResearchAdmin)

# change the title and header of the admin site
admin.site.site_header = "College Research Administration"
admin.site.site_title = "Research Admin Portal"
admin.site.index_title = "Welcome to the Research Admin Dashboard"
