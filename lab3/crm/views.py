from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET", "POST"])

def index(request):
    return render(request, "home.html")


def art_shop_profile(request):
    return JsonResponse({'Stub': 'Profile stub!'})


def arts_list(request):
    return JsonResponse({'Stub': 'Stub for the list of works of arts!'})


def categories(request):
    return JsonResponse({'Stub': 'Stub for category page!'})


def category(request, id_category):
    return JsonResponse({'Stub': 'Stub for category №%s' % id_category})
