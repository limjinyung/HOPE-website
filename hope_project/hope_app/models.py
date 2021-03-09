from django.db import models
from django.db import models
from django.contrib.auth.models import User

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
        return self.quote_id


class VolunteerExperience(models.Model):
    # portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    volunteer_experience_id = models.AutoField(primary_key=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.volunteer_experience_id


class WorkExperience(models.Model):
    # portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    work_experience_id = models.AutoField(primary_key=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.work_experience_id


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=100)
    biography = models.CharField(max_length=500)
    work_experience = models.ForeignKey('WorkExperience', null=True, blank=True, on_delete=models.CASCADE)
    volunteer_experience = models.ForeignKey('VolunteerExperience', null=True, blank=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    portfolio_image = models.ImageField(null=True, blank=True, upload_to='portfolios')

    def __str__(self):
        return str(self.portfolio_id)


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
    post_image = models.ImageField(null=True, blank=True, upload_to='posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ", " + self.content + ", " + self.slug + ", " + \
               self.created_on.strftime("%m/%d/%Y, %H:%M:%S") + ", " + \
               self.updated_on.strftime("%m/%d/%Y, %H:%M:%S") + ", " + str(self.status)


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