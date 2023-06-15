from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100)
    github_repo_link = models.URLField()
    pythonanywhere_link = models.URLField()

class Area(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    areas_of_interest = models.ManyToManyField(Area, through='AuthorArea')

class AuthorArea(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.URLField()
    link = models.URLField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)




