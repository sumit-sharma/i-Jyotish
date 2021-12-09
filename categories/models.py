from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = 'categories'    
    