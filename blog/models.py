from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
#Tages
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
#posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name="posts")
    status = models.CharField(max_length=10,choices=[('draft','Draft'),('published','Puhlished')],default='draft')
    def __str__(self):
        return self.title
    class Meta:
        ordering =['-published_at']
