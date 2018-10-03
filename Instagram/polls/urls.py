from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('usuarios/', views.index, name='index'),
    path('post/', views.post, name='post'),
   
    # ex: /polls/5/
    path('<int:user_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:user_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:user_id>/vote/', views.vote, name='vote'),

]