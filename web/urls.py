from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from .views import set_language_from_url
from django.conf import settings
from django.conf.urls.static import static
from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('social/', include('social_django.urls', namespace='social')),
    #forum urls
    path('i18n/', include('django.conf.urls.i18n')),
    path("set_language/<str:user_language>/", set_language_from_url, name="set_language_from_url"),
    path('forum/', include(machina_urls)),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
    # API urls
    path('api-blog/', include('blog.api.urls')),
    # Blog urls
    path('', include('blog.urls')),
    # Authentication Urls
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Resete Password Urls
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    # Change Password Urls
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

    path('', include('blog.urls')),
