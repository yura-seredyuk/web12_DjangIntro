from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def image_tag(self):
    #     from django.utils.html import escape
    #     return u'<img src="%s" />' % escape('users/%Y/%m/%d/')
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

    def __str__(self):
       return f"{self.author} {self.title}" 
