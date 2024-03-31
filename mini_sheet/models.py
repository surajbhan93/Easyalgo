from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
class mini_sheet(models.Model):
    ACTIONS = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Revisit', 'Revisit'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    gfg_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="GeeksforGeeks Link")
    leetcode_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="LeetCode Link")
    youtube_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="YouTube Link")
    notes_pdf_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Notes PDF Link")
    action = models.CharField(max_length=20, choices=ACTIONS, default='Pending')
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='miniblog')

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        # Generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mini_detail', args=[self.slug])

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(mini_sheet, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
