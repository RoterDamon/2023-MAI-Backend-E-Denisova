from django.urls import path
from project import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.art_shop_profile, name='user-profile'),
    path('arts_list', views.arts_list, name='arts_list'),
    path('category/<int:id_category>/', views.categories, name='categories'),
    path('add', views.add_genre, name='genre'),
]