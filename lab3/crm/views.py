from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, "home.html")


def art_shop_profile(request):
    user_profile = {
        'username': 'Kate',
        'email': 'kate@gmail.com',
        'age': 21,
        'gender': 'female',
        'location': 'Russia'
    }
    return JsonResponse(user_profile)


def arts_list(request):
    if request.method == "GET":
        art_id_1 = request.GET.get("art_id", 1)
        pic_1 = request.GET.get("name", "Morning in the pine forest")
        artist_1 = request.GET.get("artist", "Ivan Ivanovich Shishkin")
        genre_1 = request.GET.get("genre", "Landscape")
        art_id_2 = request.GET.get("art_id", 2)
        name_2 = request.GET.get("name", "In the Blue Expanse")
        artist_2 = request.GET.get("artist", "Arkady Alexandrovich Rylov")
        genre_2 = request.GET.get("genre", "Seascape")
        return JsonResponse({"All arts": [{"art_id": art_id_1, "name": pic_1, "artist": artist_1, "genre": genre_1},
                                          {"art_id": art_id_2, "name": name_2, "artist": artist_2, "genre": genre_2}]})
    else:
        return HttpResponseBadRequest("<h2>Invalid request method!</h2>")


def categories(request):
    if request.method == 'GET':
        genre_categories = ['Landscape', 'Seascape', 'Portrait', 'Still-life']
        return JsonResponse(genre_categories, safe=False)
    else:
        return HttpResponseBadRequest("<h2>Invalid request method!</h2>")


@csrf_exempt  # разрешаем делать POST запрос без куки
def add_genre(request):
    if request.method == "POST":
        genre_id = request.GET.get("genre_id", 5)
        name = request.GET.get("name", "Historical")
        return JsonResponse({"genre_id": genre_id, "name": name})
    else:
        return HttpResponseBadRequest("<h2>Invalid request method!</h2>")
