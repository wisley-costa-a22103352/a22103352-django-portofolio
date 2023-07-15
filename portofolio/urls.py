#  hello/urls.py

from django.urls import path, include
from . import views
from portofolio.views import post_list, post_create, post_update, post_delete

app_name = 'portofolio'

urlpatterns = [

    path('', views.Hero_Page, name='Hero_Page'),
    path('Escolas', views.Escolas, name='Escolas'),
    path('Engeharia_Informática', views.nova_inscricao, name='Engeharia_Informática'),
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
    path('cidade', views.cidade, name='cidade'),

    path('', views.home_page_view, name='home'),
    path('nova/', views.nova_tarefa_view, name='nova'),
    path('edita/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),

    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),

    # URLs de autenticação
    path('accounts/', include('django.contrib.auth.urls')),  # Adicione esta linha
]
