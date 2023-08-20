from django.db import models
from django_quill.fields import QuillField
 

# Create your models here.
from blog.models import BaseModel



class App(BaseModel):
    name= models.CharField(max_length=255)
    description=models.TextField()
    icon=models.ImageField( upload_to='static\images', height_field=None, width_field=None, max_length=None)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AppFeature(BaseModel):
    app_id = models.ForeignKey("apps.App", verbose_name=("ID"), on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    short_description = models.TextField()
    content = QuillField()
    icon = models.ImageField(upload_to='static\images', height_field=None, width_field=None, max_length=None)
    is_active =models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Pricing(BaseModel):
    title= models.CharField(max_length=250)
    short_description=models.TextField()
    monthly_bill=models.FloatField()
    annual_bill=models.FloatField()

    def __str__(self):
        return self.title

class PlanFeature(BaseModel):
    name= models.CharField( max_length=250)
    description =models.TextField()

    def __str__(self):
        return self.name


class PricingPlanFeature(BaseModel):
    app_id=models.ForeignKey("apps.App",verbose_name=("APP NAME"),on_delete=models.CASCADE)
    feature_id=models.ForeignKey("apps.AppFeature",verbose_name=("APP FEATURE NAME"),on_delete=models.CASCADE)
    pricing_id=models.ForeignKey("apps.Pricing",verbose_name=("PRICING"),on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)