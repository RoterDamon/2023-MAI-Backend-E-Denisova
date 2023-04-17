from django.urls import path

from crm import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('arts_list', views.arts_list, name='arts_list'),
    path('categories', views.categories, name='categories'),
    path('add', views.add_genre, name='genre'),
]
