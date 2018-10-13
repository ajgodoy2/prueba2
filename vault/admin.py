from django.contrib import admin

from .models import User
from django.contrib.auth.admin import UserAdmin
from books.admin import ReviewWriterInline


class NewUserAdmin(UserAdmin):
    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    inlines = (ReviewWriterInline,)


# Register your models here.
admin.site.register(User, NewUserAdmin)
