from django.urls import path
from . import views
from .views import UserRegisterWizard
from .forms import EmailForm, PasswordForm, NameForm

app_name = 'autenticacao'

urlpatterns = [
    path('', views.login, name='login'),
    path("cadastro/", UserRegisterWizard.as_view([EmailForm, PasswordForm, NameForm]), name="cadastro"),
    path('logout/', views.logout_view, name='logout'),
]