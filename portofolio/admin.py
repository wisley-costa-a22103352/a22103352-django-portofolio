from django.contrib import admin
from .models import Article, Author, Area, AuthorArea, Blog, Like

admin.site.register(Area)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(AuthorArea)
admin.site.register(Like)
