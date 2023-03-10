"""DatingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from dating.views import UserCRUDView,InterestsCRUDView,GetInterestsByUserIdView,MatchView,LikesView,DisLikesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_crud/',UserCRUDView.as_view()),
    path('user_crud_pk/<int:pk>/',UserCRUDView.as_view()),

    path('interests_crud/',InterestsCRUDView.as_view()),
    path('interests_crud_pk/<int:pk>/',InterestsCRUDView.as_view()),
    path('get_interests_by_user_id/<int:pk>/',GetInterestsByUserIdView.as_view()),

    path('match_view/',MatchView.as_view()),

    path('add_like/',LikesView.as_view()),
    path('get_likes_by_user_id/<int:pk>/',LikesView.as_view()),

    path('add_dislike/',DisLikesView.as_view()),
    path('get_dislikes_by_user_id/<int:pk>/',DisLikesView.as_view()),


]