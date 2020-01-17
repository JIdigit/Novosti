from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=80, blank=False)
    slug = models.SlugField(max_length=80, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name




class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    image = models.ImageField(upload_to='news_images/%Y/%m/%d',
                              blank=True,
                              max_length=200,
                              )
    body = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


class Comments(models.Model):
    news = models.ForeignKey(News, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    # def __str__(self):
    #     return self.post

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_likes = models.ForeignKey(News, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.news_likes}"











