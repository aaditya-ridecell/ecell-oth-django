from django.urls import path
from . import views
app_name = 'treasurehunt'

urlpatterns = [
    path('', views.user_login, name='index'),
    path('question/', views.question, name="question"),
    path('logout/', views.user_logout, name="logout"),
    # path('login/', views.user_login, name='login'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]
