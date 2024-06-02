from django.urls import path

from games import views

urlpatterns = [
    path('',views.GamesListView.as_view(), name='games_list'),
    path('new/',views.GameRegistereView.as_view(), name='games_new'),
    path('<int:pk>/edit/',views.GameUpdateView.as_view(), name='games_edit'),
    path('<int:pk>/delete/',views.GameDeleteView.as_view(), name='games_delete'),
]
