from django.urls import path

from crm import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.art_shop_profile, name='profile'),
    path('arts_list', views.arts_list, name='arts_list'),
    path('categories', views.categories, name='categories'),
    path('category/<int:id_category>/', views.category, name='category'),
]