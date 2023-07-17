from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import forms


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

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
    photo = models.ImageField(upload_to='post_photos', null=True, blank=True)
    video = models.FileField(upload_to='post_videos', null=True, blank=True)
    video_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):  # Adiciona
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class Escolas(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    year = models.DateField(null=True, blank=True)
    degree = models.CharField(max_length=200)
    instituion = models.CharField(max_length=200)
    def __str__(self):
        return self.instituion


class Projetos(models.Model):
    foto = models.ImageField(upload_to='foto', null=True, blank=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    data = models.DateTimeField(null=True, blank=True)
    nota = models.IntegerField(default=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

