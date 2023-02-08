from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("todo.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    path("reset-password/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"),name="password_reset_complete"),

]
