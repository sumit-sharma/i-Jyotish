from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name="followed_user_id", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="following_user_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
       return f"{self.user_id} follows {self.following_user_id}"
    

    class Meta:
        db_table = 'followers'
        verbose_name_plural = "followers"
        # constraints = [
        #     models.UniqueConstraint(fields=['user_id','following_user_id'],  name="unique_followers")
        # ]
        ordering = ["-created_at"]

    
    
    