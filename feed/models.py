from django.db import models


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
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='news_images/%Y/%m/%d', blank=True)
    body = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title














