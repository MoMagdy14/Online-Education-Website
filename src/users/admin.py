from django.contrib import admin
from .models import User, Role

# Register your models here.
#admin.site.register(User)

admin.site.register(Role)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "phone")
    list_filter = ("email", "username", "phone")
    search_fields = ("email", "username", "phone")