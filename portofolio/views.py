from django.shortcuts import render

from portofolio.models import Area, Author, Article, Blog


# Create your views here.

def Escolas(request):
    return render(request, 'portofolio/Escolas.html')


def Engeharia_Informatica(request):
    return render(request, 'portofolio/Engeharia_Informática.html')

def Experiencia_Profissional(request):
    return render(request, 'portofolio/Experiencia_Profissional.html')

def Hero_Page(request):
    return render(request, 'portofolio/Hero_Page.html')

def home(request):
    return render(request, 'portofolio/home.html')


def Interesses_e_Hobbies(request):
    return render(request, 'portofolio/Interesses _e_Hobbies.html')

def layout(request):
    return render(request, 'portofolio/layout.html')


def Licenciatura(request):
    return render(request, 'portofolio/Licenciatura.html')


def Linguisticas(request):
    return render(request, 'portofolio/Linguísticas.html')

def Organizativas(request):
    return render(request, 'portofolio/Organizativas.html')

def Projetos(request):
    return render(request, 'portofolio/Projetos.html')

def Sociais(request):
    return render(request, 'portofolio/Sociais.html')

def Tecnicas(request):
    return render(request, 'portofolio/Técnicas.html')

def Projetos(request):
    return render(request, 'portofolio/Projetos.html')

def Tecnologias(request):
    return render(request, 'portofolio/Tecnologias.html')

def Padroes(request):
    return render(request, 'portofolio/Padrões.html')

def Contactos(request):
    return render(request, 'portofolio/Contactos.html')

def Laboratorios (request):
    return render(request, 'portofolio/Laboratorios.html')

def front_end (request):
    return render(request, 'portofolio/front-end.html')

def back_end(request):
    return render(request, 'portofolio/back-end.html')


def wavesBackground (request):
    return render(request, 'portofolio/wavesBackground.html')


def blog(request):
    blog = Blog.objects.first()  # Obtém o primeiro blog (você pode ajustar isso conforme necessário)
    areas = Area.objects.all()
    autores = Author.objects.all()
    artigos = Article.objects.all()

    context = {
        'blog': blog,
        'areas': areas,
        'autores': autores,
        'artigos': artigos,
    }

    return render(request, 'portofolio/Blog.html', context)

