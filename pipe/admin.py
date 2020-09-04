from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from . import models


class PipeImageInline(admin.TabularInline):
    model = models.PipeImageModel
    extra = 0


class PipeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = models.PipeModel
        fields = '__all__'


class PipeAdmin(admin.ModelAdmin):
    form = PipeAdminForm
    inlines = [PipeImageInline]


admin.site.register(models.PipeModel, PipeAdmin)
