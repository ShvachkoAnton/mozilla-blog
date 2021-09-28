
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
# Create your models here.
STATUS=((0,"Draft"),
(1, "Publish")
)

class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0)
    class Meta:
        ordering=['-created_on']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile",
    on_delete=models.CASCADE)
    bio=models.TextField(max_length=200)
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,
    related_name='comments')
    body=models.CharField(max_length=250)
    created_on=models.DateField(auto_now_add=True)
    class Meta:
        ordering=('created_on',)
        
