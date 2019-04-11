from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
                    upload_to="posts/images",
                    processors=[ResizeToFill(800,600)],
                    format='JPEG',
                    options={'quality':90},
                    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    