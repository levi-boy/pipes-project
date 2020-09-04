from django.contrib import admin

from . import models


class PipeImageInline(admin.TabularInline):
    model = models.PipeImageModel
    extra = 0


class PipeAdmin(admin.ModelAdmin):
    inlines = [PipeImageInline]


admin.site.register(models.PipeModel, PipeAdmin)
