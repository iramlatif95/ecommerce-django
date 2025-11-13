from django.urls import path
from django.contrib.auth import views as auth_views 
from.import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('profile/',views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/login_user/'  
    ),
    name='password_reset_confirm' 
),


# email is sent
path(
    'password_reset_done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'  # create this template
    ),
    name='password_reset_done'
),




]