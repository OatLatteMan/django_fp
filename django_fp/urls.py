from django.urls import path
from django_fp import views

app_name = 'django_fp'

urlpatterns = [
    # http://127.0.0.1:[PORT]/final_project
    path('', views.home, name='home'),

    # http://127.0.0.1:[PORT]/final_project/films
    # path('films/', views.list, name='films'),

    # http://127.0.0.1:[PORT]/final_project/films
    path('films/', views.ItemList.as_view(), name='films'),

    # http://127.0.0.1:[PORT]/final_project/actors
    path('actors/', views.actors, name='actors'),

    # http://127.0.0.1:[PORT]/final_project/detail
    # path('<int:number>/', views.detail, name='detail'),

    # http://127.0.0.1:[PORT]/final_project/detail
    path('films/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),

    # http://127.0.0.1:[PORT]/final_project/new
    path('new', views.django_fp_new, name='new'),
]

