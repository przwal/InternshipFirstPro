from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blogTitle = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Add this line for image upload
    blogDescription = models.TextField()  # Use TextField for longer text
    blogCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.blogTitle