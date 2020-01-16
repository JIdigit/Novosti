from django.urls import path
from .views import *


urlpatterns = [
    path('', news_list, name='news_list'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    # path(finctioc, name='login')
]