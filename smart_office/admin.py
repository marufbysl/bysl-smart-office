from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Fqa)
class FqaAdmin(admin.ModelAdmin):

    list_display=('feature_id','created_by', 'updated_by')
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
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
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

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display=['customer_id','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=['first_name','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=['email','created_by','updated_by']
    readonly_fields = ['created_by','updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:

            obj.created_by = request.user
        else:
            # Existing object is being changed, update the updated_by field
            obj.updated_by = request.user
            print(request.user)
        super().save_model(request, obj, form, change)