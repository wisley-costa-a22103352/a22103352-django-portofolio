#  hello/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'portofolio'

urlpatterns = [

    path('', views.hero_page, name='Hero_Page'),

    path('escolas/', views.escola_list, name='escola_list'),
    path('escolas/create/', views.escola_create, name='escola_create'),
    path('escolas/update/<int:pk>/', views.escola_update, name='escola_update'),
    path('escolas/delete/<int:pk>/', views.escola_delete, name='escola_delete'),

    path('Engeharia_Informática', views.nova_inscricao, name='Engeharia_Informática'),

    path('Experiencia_Profissional', views.experiencia_profissional, name='Experiencia_Profissional'),

    path('home', views.home, name='home'),

    path('Interesses _e_Hobbies', views.interesses_e_hobbies, name='Interesses _e_Hobbies'),

    path('Licenciatura', views.licenciatura, name='Licenciatura'),

    path('Linguística', views.linguisticas, name='Linguística'),

    path('Organizativas', views.organizativas, name='Organizativas'),

    path('projetos/', views.projeto_list, name='projeto_list'),
    path('projetos/create/', views.projeto_create, name='projeto_create'),
    path('projetos/update/<int:pk>/', views.projeto_update, name='projeto_update'),
    path('projetos/delete/<int:pk>/', views.projeto_delete, name='projeto_delete'),

    path('Sociais', views.sociais, name='Sociais'),

    path('Técnicas', views.tecnicas, name='Técnicas'),

    path('Tecnologias', views.tecnologias, name='Tecnologias'),

    path('Padrões', views.padroes, name='Padrões'),

    path('Laboratorios', views.laboratorios, name='Laboratorios'),

    path('Contactos', views.contactos, name='Contactos'),

    path('front-end', views.front_end, name='front-end'),
    path('back-end', views.back_end, name='back-end'),

    path('wavesbackground', views.wavesbackground, name='wavesbackground'),

    path('cidade', views.cidade, name='cidade'),

    path('home', views.home_page_view, name='home'),
    path('nova/', views.nova_tarefa_view, name='nova'),
    path('edita/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),

    path('login/', LoginView.as_view(template_name='portofolio/Autenticacao/login.html'), name='login'),
    path('post_list/', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),

    path('calculadora', views.calculadora, name='calculadora'),
    path('calculadora-cientifica/', views.calculadora_cientifica, name='calculadora_cientifica'),

    path("accounts/", include("django.contrib.auth.urls")),
    # Com esta rota temos acesso a todos os padrões URL (Login, Logout...)
    path('register/', views.register, name='register'),

    path('weather', views.weather, name='weather'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
