from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [ 
   path("", views.VaultView.as_view(), name="home"),
   path("register", views.CreateAccount.as_view(), name="register"),
   path("add/account", views.AddAccountView.as_view(), name='add'),
    path("delete/account/<int:pk>", views.DeleteAccView.as_view(), name="delete_acc"),
    path("update/account/<int:pk>", views.UpdateAccView.as_view(), name="update_acc"),
    path("login", auth_views.LoginView.as_view(template_name="vault/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="vault/logout.html"), name="logout"),
]