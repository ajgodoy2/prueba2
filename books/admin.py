from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from vault.models import User
from .models import ReviewWriter, Author, Book, Review
from django import forms


class ReviewAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Review
        widgets = {'opinion': forms.Textarea}


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('book', 'writer', 'rating')


class ReviewWriterInline(admin.StackedInline):
    model = ReviewWriter
    can_delete = False
    verbose_name = 'review writer'


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review, ReviewAdmin)
