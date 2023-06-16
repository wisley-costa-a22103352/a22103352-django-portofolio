#  hello/urls.py

from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [

    path('', views.Hero_Page, name='Hero_Page'),
    path('Escolas', views.Escolas, name='Escolas'),
    path('Engeharia_Informática', views.Engeharia_Informatica, name='Engeharia_Informática'),
    path('Experiencia_Profissional', views.Experiencia_Profissional, name='Experiencia_Profissional'),
    path('home', views.home, name='home'),
    path('Interesses _e_Hobbies', views.Interesses_e_Hobbies, name='Interesses _e_Hobbies'),
    path('layout', views.layout, name='layout'),
    path('Licenciatura', views.Licenciatura, name='Licenciatura'),
    path('Linguística', views.Linguisticas, name='Linguística'),
    path('Organizativas', views.Organizativas, name='Organizativas'),
    path('Projetos', views.Projetos, name='Projetos'),
    path('Sociais', views.Sociais, name='Sociais'),
    path('Técnicas', views.Tecnicas, name='Técnicas'),
    path('Tecnologias', views.Tecnologias, name='Tecnologias'),
    path('Padrões', views.Padroes, name='Padrões'),
    path('Laboratorios', views.Laboratorios, name='Laboratorios'),
    path('Contactos', views.Contactos, name='Contactos'),
    path('front-end', views.front_end, name='front-end'),
    path('back-end', views.back_end, name='back-end'),
    path('blog', views.blog, name='blog'),


    path('wavesBackground', views.wavesBackground, name='wavesBackground'),

]
