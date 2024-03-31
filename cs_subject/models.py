from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class cs_subject(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='csblog')

    def number_of_likes(self):
        return self.likes.count()
    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('cd_detail', args=[self.slug])

    class Meta:
    	ordering = ['-date_added']



class Comment(models.Model):
    post = models.ForeignKey(cs_subject, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
