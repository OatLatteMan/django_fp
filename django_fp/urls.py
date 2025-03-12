from django.urls import path
from final_project import views

app_name = 'final_project'

urlpatterns = [
    # http://127.0.0.1:[PORT]/final_project
    path('', views.home, name='home'),

    # http://127.0.0.1:[PORT]/final_project/films
    path('films/', views.films_serials, name='films'),

    # http://127.0.0.1:[PORT]/final_project/actors
    path('actors/', views.actors, name='actors'),

    # http://127.0.0.1:[PORT]/final_project/detail
    path('<int:number>/', views.detail, name='detail'),

    # http://127.0.0.1:[PORT]/final_project/new
    path('new', views.final_project_new, name='new'),
]

