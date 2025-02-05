from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path('partial_matches/', views.partial_matches, name='partial_matches'),
    path('newpage/',views.new_page,name="newpage"),
    path('<str:entry>/',views.renderEntry,name="entry"),
    path('search',views.search,name="search"),  
    path('create',views.create,name="create"),   
]
