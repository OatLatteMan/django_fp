from django.urls import path
from django_fp import views

app_name = 'django_fp'

urlpatterns = [
    # http://127.0.0.1:[PORT]/django_fp
    path('', views.home, name='home'),

    # http://127.0.0.1:[PORT]/django_fp/films
    path('films/', views.ItemList.as_view(), name='films'),

    # http://127.0.0.1:[PORT]/django_fp/detail
    path('films/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),

    # http://127.0.0.1:[PORT]/django_fp/actors
    path('actors/', views.ActorList.as_view(), name='actors'),

    # http://127.0.0.1:[PORT]/django_fp/actors
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),

    # http://127.0.0.1:[PORT]/django_fp/new
    path('new', views.django_fp_new, name='new'),
]

