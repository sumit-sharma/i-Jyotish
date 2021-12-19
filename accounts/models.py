from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import Category

# Create your models here.


class User(AbstractUser):
    email_verified_at = models.DateTimeField(auto_now_add=True, null=True)
    country_code = models.CharField(_("country code"), max_length=15, blank=True)
    mobile_no = models.CharField(_("mobile number"), max_length=12, blank=True)
    phone_verified_at = models.DateTimeField(auto_now_add=True, null=True)
    fb_id = models.CharField(max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "users"


class CategoryUser(models.Model):
    user = models.ForeignKey(User, related_name="user_id", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_id",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "category_user"
        
        