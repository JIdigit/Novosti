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


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='author', default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image = models.ImageField(upload_to='news_images/%Y/%m/%d',
                              height_field='image_height',
                              width_field='image_width',
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
    post = models.ForeignKey(News, related_name='comment', on_delete=models.CASCADE)















