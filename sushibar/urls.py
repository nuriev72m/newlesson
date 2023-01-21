from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sashimi/', sashimi, name='sashimi'),
    path('sushi/', sushi, name='sushi'),
    path('rolls/', rolls, name='rolls'),
    path('pricelist/', pricelist, name='pricelist'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
