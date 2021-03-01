from django.db import models
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self):
        return self.username


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(max_length=1500)
    slug = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField(upload_to='post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)