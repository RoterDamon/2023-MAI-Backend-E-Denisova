from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from project import models


# Create your views here.

@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, "home.html")


@require_http_methods(["GET", "POST"])
@login_required
def art_shop_profile(request):
    return render(request, 'profile.html')


@require_http_methods(["GET", "POST"])
def arts_list(request):
    if request.method == "GET":
        try:
            arts = models.Art.objects.all()
            list = []
            for art in arts:
                list.append({"art_id": art.art_id, "name": art.name_pic, "artist": art.artist.name_artist,
                             "genre": art.genre.name_genre, "date": art.creation_date, "price": art.price})
            return JsonResponse({"All arts": [list]})
        except models.Art.DoesNotExist:
            return HttpResponseBadRequest("<h2>Empty response</h2>")
    else:
        return HttpResponseBadRequest("<h2>Invalid request method!</h2>")


@require_http_methods(["GET", "POST"])
def categories(request, id_category):
    if request.method == 'GET':
        try:
            arts = models.Art.objects.filter(genre_id=id_category)
            list = []
            for art in arts:
                list.append({"art_id": art.art_id, "name": art.name_pic, "artist": art.artist.name_artist,
                             "genre": art.genre.name_genre, "date": art.creation_date, "price": art.price})
            return JsonResponse({"All arts in this category": [list]})
        except models.Art.DoesNotExist:
            return HttpResponseBadRequest("<h2>Empty response</h2>")
    else:
        return HttpResponseBadRequest("<h2>Invalid request method!</h2>")


@csrf_exempt  # разрешаем делать POST запрос без куки
@require_http_methods(["GET", "POST"])
def add_genre(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})

        try:
            genre = models.Genre()
            genre.name_genre = name

            exists = True
            try:
                _ = models.Genre.objects.get(name_genre=name)
            except models.Genre.DoesNotExist:
                exists = False
            except models.Genre.MultipleObjectsReturned:
                pass

            if not exists:
                genre.save()
            return JsonResponse({"status": ("OK" if not exists else "Already exists")})
        except:
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")
