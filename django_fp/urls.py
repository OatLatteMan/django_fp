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
    path('films/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),

    # http://127.0.0.1:[PORT]/django_fp/actors/[actor.id]
    path('actors/', views.ActorList.as_view(), name='actors'),

    # http://127.0.0.1:[PORT]/django_fp/actors/[actor.id]
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),

    # http://127.0.0.1:[PORT]/django_fp/new
    path('new_film/', views.django_fp_new_film, name='new_film'),

    # http://127.0.0.1:[PORT]/django_fp/new
    path('new_actor/', views.django_fp_new_actor, name='new_actor'),

    # http://127.0.0.1:[PORT]/django_fp/films/[item.id]/delete
    path('<int:number>/delete_film/', views.django_fp_delete_item, name='item_delete'),

    # http://127.0.0.1:[PORT]/django_fp/actors/[actor.id]/delete
    path('<int:number>/delete_actor/', views.django_fp_delete_actor, name='actor_delete'),

    # http://127.0.0.1:[PORT]/django_fp/[item.id]/edit
    path('films/<int:pk>/edit', views.ItemUpdate.as_view(), name='item_edit'),

    # http://127.0.0.1:[PORT]/django_fp/[actor.id]/edit
    path('actors/<int:pk>/edit', views.ActorUpdate.as_view(), name='actor_edit'),

    # http://127.0.0.1:[PORT]/django_fp/profile
    path('profile/', views.profile_view, name='profile'),

    # http://127.0.0.1:[PORT]/django_fp/profile/edit
    path('profile/edit', views.profile_edit, name='edit_profile'),

    # http://127.0.0.1:[PORT]/django_fp/popular_actors
    path('actors/popular/', views.PopularActorListView.as_view(), name='popular_actors'),

    # http://127.0.0.1:[PORT]/django_fp/search/actors
    path('search/actors', views.actor_search, name='search_actors'),

    # http://127.0.0.1:[PORT]/django_fp/search/suggestions
    path('search/item_suggestions/', views.search_item_suggestions, name='search_suggestions'),

]

