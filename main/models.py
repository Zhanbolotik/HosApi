from django.db import models

from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=300)
    full_name = models.CharField(max_length=100,default='Anonimous')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=150, default='Bishkek')
    phone = models.CharField(max_length=15, default='+996700000000')


    def __str__(self):
        return self.title

class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
