from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from portofolio.models import Area, Author, Article, Blog, Cidade, Tarefa, Post
from .forms import Inscricao_form, TarefaForm, PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscricao
from django.contrib.auth.decorators import login_required


# Create your views here.

def Escolas(request):
    return render(request, 'portofolio/Sobre_Mim/Escolas.html')


def Engeharia_Informatica(request):
    return render(request, 'portofolio/Sobre_Mim/Engeharia_Informática.html')


def Experiencia_Profissional(request):
    return render(request, 'portofolio/Sobre_Mim/Experiencia_Profissional.html')


def Hero_Page(request):
    return render(request, 'portofolio/Landing_Page/Hero_Page.html')


def home(request):
    return render(request, 'portofolio/Tarefas/home.html')


def Interesses_e_Hobbies(request):
    return render(request, 'portofolio/Sobre_Mim/Interesses _e_Hobbies.html')


def layout(request):
    return render(request, 'portofolio/layout.html')


def Licenciatura(request):
    return render(request, 'portofolio/Sobre_Mim/Licenciatura.html')


def Linguisticas(request):
    return render(request, 'portofolio/Sobre_Mim/Linguísticas.html')


def Organizativas(request):
    return render(request, 'portofolio/Sobre_Mim/Organizativas.html')


def Projetos(request):
    return render(request, 'portofolio/Projetos/Projetos.html')


def Sociais(request):
    return render(request, 'portofolio/Sobre_Mim/Sociais.html')


def Tecnicas(request):
    return render(request, 'portofolio/Sobre_Mim/Técnicas.html')


def Projeto(request):
    return render(request, 'portofolio/Projetos/Projetos.html')


def Tecnologias(request):
    return render(request, 'portofolio/Sobre_Website/Tecnologias.html')


def Padroes(request):
    return render(request, 'portofolio/Sobre_Website/Padrões.html')


def Contactos(request):
    return render(request, 'portofolio/Contactos/Contactos.html')


def Laboratorios(request):
    return render(request, 'portofolio/Programacao_Web/Laboratorios.html')


def front_end(request):
    return render(request, 'portofolio/Programacao_Web/front-end.html')


def back_end(request):
    return render(request, 'portofolio/Programacao_Web/back-end.html')


def wavesBackground(request):
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

    return render(request, 'portofolio/Blog/Blog.html', context)


def cidade(request):
    zona = Cidade.objects.all()
    return render(request, 'portofolio/Defesa/cidade.html', zona)


def nova_inscricao(request):
    form = Inscricao_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portofolio:Engeharia_Informática')
    context = {'form': form}

    return render(request, 'portofolio/Sobre_Mim/Engeharia_Informática.html', context)




# Create your views here.


def home_page_view(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'portofolio/Tarefas/home.html', context)


def nova_tarefa_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portofolio:home')

    context = {'form': form}

    return render(request, 'portofolio/Tarefas/nova.html', context)


def edita_tarefa_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portofolio:home'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'portofolio/Tarefas/edita.html', context)


def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portofolio:home'))


def post_list(request):
    context = {'posts': Tarefa.objects.all()}
    return render(request, 'portofolio/Blog/post_list.html', context)

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'portofolio/Blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'portofolio/Blog/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'portofolio/Blog/post_confirm_delete.html', {'post': post})
