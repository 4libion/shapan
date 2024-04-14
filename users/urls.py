from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    RegisterView,
    UserView,
    UserAddArticlesView,
    UserAddRoadmapView,
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('articles', UserAddArticlesView.as_view()),
    path('roadmap', UserAddRoadmapView.as_view()),
]
