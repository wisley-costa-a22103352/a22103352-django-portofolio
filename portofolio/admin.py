from django.contrib import admin
from .models import Cidade, Inscricao, Tarefa, Post, Escolas, Projetos
from django.contrib.auth.models import User
from django.contrib.auth import forms


admin.site.register(Cidade)
admin.site.register(Inscricao)
admin.site.register(Tarefa)
admin.site.register(Post)
admin.site.register(Escolas)
admin.site.register(Projetos)


# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):  # Adiciona
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'