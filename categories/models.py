from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'categories'    
    