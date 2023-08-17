from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,User
from django.conf import settings
# Create your models here
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='+',null=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='+',null=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(max_length=300)
    content = QuillField()
    image =models.ImageField()
    category_id = models.ForeignKey('blog.BlogCategory', verbose_name="Category",on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField('blog.BlogTag', verbose_name="tags")
    
    def __str__(self):
        return self.title

class BlogTag(BaseModel):
    name =  models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.name
    
class BlogCategory(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name
    
