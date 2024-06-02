from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import QuerySet
from games.models import Games, Profile
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

#INDEX
def inicio(request):
    return render(request, 'games_list.html')

#Nuevo usuario

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            messages.success(request, 'done')
            new_user = f.save()

            # logueo automático
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            Profile.objects.create(
                id_de_usuario_id=request.user.id, birth_date="2010-01-01")

            return render(request, 'games_list')
    else:
        f = CustomUserCreationForm()
    return render(request, 'games/register.html', {'form': f})


#Lista de juegos
class GamesListView(generic.ListView):
    model = Games
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        q=self.request.GET.get('q')
        
        if q:
            return Games.objects.filter(Game_name__icontains=q)

        return super().get_queryset()

class GameRegistereView(generic.CreateView):
    model = Games
    fields = ('avatar','Game_name', 'Game_lang', 'Game_engine','Game_description', 'Game_dev', 'dev_email', 'Game_link')
    success_url = reverse_lazy('games_list')

class GameUpdateView(generic.UpdateView):
    model = Games
    fields = ('avatar','Game_name', 'Game_lang', 'Game_engine','Game_description', 'Game_dev', 'dev_email', 'Game_link')
    success_url = reverse_lazy('games_list')

class GameDeleteView(generic.DeleteView):
    model = Games
    success_url = reverse_lazy('games_list')
    