from django.urls import path
from .views import *


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search'),
    path('', news_list, name='news_list'),
    path('news_list/<slug:category_slug>/', news_list, name='news_list_slug'),
    path('categories/', CategorListView.as_view(), name='category'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('login/', user_login, name='login'),
    path('register', user_register, name='registration'),
    path('logout/', user_logout, name='logout'),
    path('create_news/' , news_create, name='news_create'),

    ]