from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from core.views import AddRememberView, HomeView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("addremember/", AddRememberView.as_view(), name="addremember"),
    path("", HomeView.as_view(), name="home"),
]
