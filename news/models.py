from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class News(models.Model):
    news_title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    news_photo = models.ImageField(upload_to='news_auto/%Y/%m/%d/')

    def __str__(self):
        return self.news_title
