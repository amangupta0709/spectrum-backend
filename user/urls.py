from django.urls import path
from knox import views as knox_views

from user.views import LoginAPIView, UserDetailsAPIView, UserRoundsAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("details/", UserDetailsAPIView.as_view(), name="user_details"),
    path("rounds/", UserRoundsAPIView.as_view(), name="user_rounds"),
]
