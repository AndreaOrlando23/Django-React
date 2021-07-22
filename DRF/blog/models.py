from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    # by defeult, instead of running all objects we can ran only post objects
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # on_delete=models.PROTECT >> if we are going to delete a category we'll not delete the posts
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # instead of using the id we can "sluggify" the title to identify each post
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    # on_delete=models.CASCADE >> if we are going to delete a User we'll delete the posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
