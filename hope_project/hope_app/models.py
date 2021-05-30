from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Quote(models.Model):
    quote_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)

    def __str__(self):
        return self.author.username + ' , ' + str(self.quote_id)


class VolunteerExperience(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    volunteer_experience_id = models.AutoField(primary_key=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.portfolio.author.username + " , " + str(self.volunteer_experience_id)


class WorkExperience(models.Model):
    portfolio = models.ForeignKey('Portfolio', null=True, on_delete=models.CASCADE)
    work_experience_id = models.AutoField(primary_key=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.portfolio.author.username + " , " + str(self.work_experience_id)


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=100)
    biography = models.CharField(max_length=500)
    # work_experience = models.ForeignKey('WorkExperience', null=True, blank=True, on_delete=models.CASCADE)
    # volunteer_experience = models.ForeignKey('VolunteerExperience', null=True, blank=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    portfolio_image = models.ImageField(null=True, blank=True, upload_to='portfolios')

    def __str__(self):
        return self.author.username + ' , ' + str(self.portfolio_id)


class PostTag(models.Model):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    created_on = models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField(upload_to='post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    post_image = models.ImageField(null=True, blank=True, upload_to='posts')
    tag = models.ForeignKey(PostTag, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ", " + self.content + ", " + self.slug + ", " + str(self.status)


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