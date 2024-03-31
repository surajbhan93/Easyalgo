from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
class Htmlpost(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='htmlblog')
    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('html_detail', args=[self.slug])

    def number_of_likes(self):
        return self.likes.count()
    

    class Meta:
    	ordering = ['date_added']



class Comment(models.Model):
    post = models.ForeignKey(Htmlpost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
