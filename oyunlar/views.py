from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request, sort_option=None):
    if sort_option == 'alphabetical':
        oyunlar = Game.objects.order_by('oyunIsim')
    elif sort_option == 'newest':
        oyunlar = Game.objects.order_by('-oyunCikisTarihi__cikisTarihi')
    elif sort_option == 'oldest':
        oyunlar = Game.objects.order_by('oyunCikisTarihi__cikisTarihi')
    else:
        oyunlar = Game.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        oyunlar = Game.objects.filter(
            Q(oyunIsim__icontains = search) |
            Q(oyunPlatformu__platform__icontains = search) |
            Q(oyunTuru__tur__icontains = search)
        )
    game_count = Game.objects.count()

    for oyun in oyunlar:
        if len(oyun.oyunAciklama) > 300:
            oyun.oyunAciklama = oyun.oyunAciklama[:300] + '...'

    context = {
        'oyunlar':oyunlar,
        'search':search,
        'game_count':game_count,
        'sort_option':sort_option
    }
    return render(request, 'index.html', context)

def games(request, gameId):
    mygame = Game.objects.get(id = gameId)
    comments = Comment.objects.filter(commentedGame=mygame)
    context = {
        'gameItem':mygame,
        'comments':comments
    }
    return render(request, 'detail.html', context)

def addGames(request):
    # pass the request object to the form when creating it
    form = GameForm(request=request)
    if request.method == 'POST':
        # pass the request object to the form when validating it
        form = GameForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'add.html', context)

def game_count(request):
    count = Game.objects.count()
    response = JsonResponse({'count':count})

    print(response)

    return response

def game_comments(request, gameId):
    game = Game.objects.get(id=gameId)
    comments = Comment.objects.filter(commentedGame=game)
    context = {
        'game': game,
        'comments': comments,
    }
    return render(request, 'comments.html', context)

def create_comment(request, gameId):
    game = None # Set a default value for the 'game' variable
    if request.method == 'POST':
        content = request.POST['content']
        commenter = request.user
        game = Game.objects.get(id=gameId)

        comment = Comment(content=content, commenter=commenter, commentedGame=game)
        comment.save()

        return redirect('details', gameId=gameId)
    else:
        try:
            game = Game.objects.get(id=gameId)
        except Game.DoesNotExist:
            # Handle the case when the game with the given ID does not exist
            pass
    context = {
        'gameId': gameId,
        'game':game
    }
    return render(request, 'create_comment.html',context)

def all_comments(request):
    comments = Comment.objects.all()
    context = {
        'comments':comments
    }
    return render(request, 'all_comments.html',context)

@login_required
def user_game_count(request):
    user = request.user
    count = Game.objects.filter(user=user).count()
    return JsonResponse({'count':count})

def user_games(request):
    user = request.user
    userGames = Game.objects.filter(user=user)
    count = Game.objects.filter(user=user).count()

    for oyun in userGames:
        if len(oyun.oyunAciklama) > 300:
            oyun.oyunAciklama = oyun.oyunAciklama[:300] + '...'

    context = {
        'userGames':userGames,
        'count': count
    }
    return render(request, 'user_games.html', context)

def upvote_game(request, gameId):
    game = get_object_or_404(Game, id=gameId)
    upvote, created = Upvote.objects.get_or_create(user=request.user, game=game)
    if created:
        # New upvote added
        game.upvote_count += 1
        game.save()
    return JsonResponse({'upvote_count': game.upvote_count})