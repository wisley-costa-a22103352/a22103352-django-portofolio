from django.forms import ModelForm
from .models import Inscricao, Tarefa, Post
from django import forms


class Inscricao_form(ModelForm):
    class Meta:
        model = Inscricao
        fields = '__all__'


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

        # Para um conjunto de propriedade da classe (titulo, prioridade, concluido, etc),
        # o dicionário widgets permite configurar o elemento HTML input correspondente,
        # através de um dicionario de atributos de formatação (especificação de classes, placeholder, propriedades, etc).
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
