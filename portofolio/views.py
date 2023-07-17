import requests
import datetime
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

from portofolio.models import Cidade, Tarefa, Post, Escolas, Projetos
from .forms import Inscricao_form, TarefaForm, PostForm, EscolaForm, ProjetoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .admin import CustomUserCreationForm
from django.contrib import messages


# Create your views here.

def escolas(request):
    return render(request, 'portofolio/Sobre_Mim/Escolas/escola_list.html')


def engeharia_informatica(request):
    return render(request, 'portofolio/Sobre_Mim/Engeharia_Informática.html')


def experiencia_profissional(request):
    return render(request, 'portofolio/Sobre_Mim/Experiencia_Profissional.html')

def hero_page(request):
    # Fazer a requisição GET à página de previsão do tempo
    # response = requests.get('https://www.weather.com')

    # Criar o objeto BeautifulSoup para analisar o HTML
    # soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar os elementos que contêm as informações da previsão do tempo
    # forecast_elements = soup.find_all('div', class_='forecast-item')

    # Extrair os detalhes da previsão do tempo
    # forecasts = []
    # for element in forecast_elements:
    # date = element.find('span', class_='date').text
    # temperature = element.find('span', class_='temperature').text
    # description = element.find('span', class_='description').text

    # forecast = {
    # 'date': date,
    # 'temperature': temperature,
    # 'description': description
    # }
    # forecasts.append(forecast)

    return render(request, 'portofolio/Landing_Page/Hero_Page.html')

def weather(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Lisboa'

    appid = 'fa078dcaf3f2d65ac653cf0a3e6a2472'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'city', 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day = datetime.date.today()
    return render(request, 'portofolio/weather.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})

def home(request):
    return render(request, 'portofolio/Tarefas/home.html')


def interesses_e_hobbies(request):
    return render(request, 'portofolio/Sobre_Mim/Interesses _e_Hobbies.html')


def licenciatura(request):
    return render(request, 'portofolio/Sobre_Mim/Licenciatura.html')


def linguisticas(request):
    return render(request, 'portofolio/Sobre_Mim/Linguísticas.html')


def organizativas(request):
    return render(request, 'portofolio/Sobre_Mim/Organizativas.html')


def projetos(request):
    return render(request, 'portofolio/Projetos/Projetos.html')


def sociais(request):
    return render(request, 'portofolio/Sobre_Mim/Sociais.html')


def tecnicas(request):
    return render(request, 'portofolio/Sobre_Mim/Técnicas.html')


def projeto(request):
    return render(request, 'portofolio/Projetos/Projetos.html')


def tecnologias(request):
    return render(request, 'portofolio/Sobre_Website/Tecnologias.html')


def padroes(request):
    return render(request, 'portofolio/Sobre_Website/Padrões.html')


def contactos(request):
    return render(request, 'portofolio/Contactos/Contactos.html')


def laboratorios(request):
    return render(request, 'portofolio/Programacao_Web/Laboratorios.html')


def front_end(request):
    return render(request, 'portofolio/Programacao_Web/front-end.html')


def back_end(request):
    return render(request, 'portofolio/Programacao_Web/back-end.html')


def wavesbackground(request):
    return render(request, 'portofolio/wavesbackground.html')


def cidade(request):
    context = Cidade.objects.all()
    return render(request, 'portofolio/Defesa/cidade.html', context)


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
    posts = Post.objects.all()
    return render(request, 'portofolio/Blog/post_list.html', {'posts': posts})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('portofolio:post_list')
    else:
        form = PostForm()
    return render(request, 'portofolio/Blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('portofolio:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'portofolio/Blog/post_form.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('portofolio:post_list')
    return render(request, 'portofolio/Blog/post_confirm_delete.html', {'post': post})

def calculadora(request):
    return render(request, 'portofolio/calculadoras/calculadora.html')

def calculadora_cientifica(request):
    return render(request, 'portofolio/calculadoras/calculadora-cientifica.html')



# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('portofolio:Hero_Page')

        else:
            print('invalid registration details')

    return render(request, "portofolio/Autenticacao/register.html", {"form": form})

def escola_list(request):
    posts = Post.objects.all()
    return render(request, 'portofolio/Sobre_Mim/Escolas/escola_list.html', {'posts': posts})

@login_required
def escola_create(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST, request.FILES)
        if form.is_valid():
            escola = form.save(commit=False)
            escola.save()
            return redirect('portofolio:escola_list')
    else:
        form = EscolaForm()
    return render(request, 'portofolio/Sobre_Mim/Escolas/escola_form.html', {'form': form})

@login_required
def escola_update(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        form = EscolaForm(request.POST, request.FILES, instance=escola)
        if form.is_valid():
            escola.save()
            return redirect('portofolio:escola_list')
    else:
        form = EscolaForm(instance=escola)
    return render(request, 'portofolio/Sobre_Mim/Escolas/escola_form.html', {'form': form, 'escola': escola})

@login_required
def escola_delete(request, pk):
    escola = get_object_or_404(Escolas, pk=pk)
    if request.method == 'POST':
        escola.delete()
        return redirect('portofolio:escola_list')
    return render(request, 'portofolio/Sobre_Mim/Escolas/escola_confirm_delete.html', {'escola': escola})


def projeto_list(request):
    projetos = Projetos.objects.all()
    return render(request, 'portofolio/Projetos/projeto_list.html', {'projetos': projetos})

@login_required
def projeto_create(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.author = request.user
            projeto.save()
            return redirect('portofolio:projeto_list')
    else:
        form = ProjetoForm()
    return render(request, 'portofolio/Projetos/projeto_form.html', {'form': form})

@login_required
def projeto_update(request, pk):
    projeto = get_object_or_404(Projetos, pk=pk)
    if projeto.author != request.user:
        # Implemente aqui a lógica para lidar com a tentativa de atualização por um usuário não autorizado
        return HttpResponseForbidden("Você não tem permissão para atualizar este projeto.")

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            projeto = form.save()
            return redirect('portofolio:projeto_list')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portofolio/Projetos/projeto_form.html', {'form': form, 'projeto': projeto})


@login_required
def projeto_delete(request, pk):
    projeto = get_object_or_404(Projetos, pk=pk)
    if projeto.author != request.user:
        # Implemente aqui a lógica para lidar com a tentativa de exclusão por um usuário não autorizado
        return HttpResponseForbidden("Você não tem permissão para excluir este projeto.")

    if request.method == 'POST':
        projeto.delete()
        return redirect('portofolio:projeto_list')
    return render(request, 'portofolio/Projetos/projeto_confirm_delete.html', {'projeto': projeto})