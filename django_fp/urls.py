from django.urls import path
from django_fp import views

app_name = 'django_fp'

urlpatterns = [
    # http://127.0.0.1:[PORT]/django_fp
    path('', views.index, name='index'),

    # http://127.0.0.1:[PORT]/django_fp/logout
    path('logout/', views.logout_view, name='logout'),

    # http://127.0.0.1:[PORT]/django_fp/films
    path('films/', views.ItemList.as_view(), name='films'),

    # http://127.0.0.1:[PORT]/django_fp/[item.id]
    path('films/<int:pk>', views.ItemDetail.as_view(), name='item_details'),

    # http://127.0.0.1:[PORT]/django_fp/actors
    path('actors/', views.ActorList.as_view(), name='actors'),

    # http://127.0.0.1:[PORT]/django_fp/actors
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),

    # http://127.0.0.1:[PORT]/django_fp/new
    path('new/', views.django_fp_new, name='new'),

    # http://127.0.0.1:[PORT]/django_fp/[id]/delete
    path('<int:number>/delete/', views.django_fp_delete_item, name='item_delete'),
]

