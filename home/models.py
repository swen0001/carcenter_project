from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teams/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=150)
    twitter_link = models.URLField(max_length=150)
    telegram_link = models.URLField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
