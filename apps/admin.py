from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(App)
class AppAdmin(admin.ModelAdmin):

    list_display=('name','created_by', 'updated_by')
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)
# admin.site.register(Blog,BlogAdmin)
@admin.register(AppFeature)
class AppFeatureAdmin(admin.ModelAdmin):
    list_display=['title','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display=['title','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)

@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    list_display=['name','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)