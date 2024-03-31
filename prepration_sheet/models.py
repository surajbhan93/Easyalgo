from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
class prepration_sheet(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='prgrablog')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_sheet', args=[self.slug])

    class Meta:
    	ordering = ['-date_added']



class Comment(models.Model):
    post = models.ForeignKey(prepration_sheet, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
