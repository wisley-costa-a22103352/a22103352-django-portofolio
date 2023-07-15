from django.db import models


# Create your models here.

class Blog(models.Model):
    username = models.CharField(max_length=100)


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
    link = models.URLField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    motivo = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
