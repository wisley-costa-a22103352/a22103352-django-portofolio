from django.contrib import admin
from .models import Article, Author, Area, AuthorArea, Blog, Like, Cidade, Inscricao, Tarefa, Post

admin.site.register(Area)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(AuthorArea)
admin.site.register(Like)
admin.site.register(Cidade)
admin.site.register(Inscricao)
admin.site.register(Tarefa)
admin.site.register(Post)