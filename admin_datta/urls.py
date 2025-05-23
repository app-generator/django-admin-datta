from django.urls import path
from admin_datta import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.index, name='index'),
  path('color/', views.color, name='color'),
  path('typography/', views.typography, name='typography'),
  path('feather-icon/', views.icon_feather, name='icon_feather'),
  path('sample-page/', views.sample_page, name='sample_page'),

  # Authentication
  path('accounts/login/', views.UserLoginView.as_view(), name='login'),
  path('accounts/logout/', views.logout_view, name='logout'),
  path('accounts/register/', views.register, name='register'),
  path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
  path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
      template_name='accounts/password_change_done.html'
  ), name="password_change_done"),
  path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
  path('accounts/password-reset-confirm/<uidb64>/<token>/', 
      views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
      template_name='accounts/password_reset_done.html'
  ), name='password_reset_done'),
  path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
      template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

]
