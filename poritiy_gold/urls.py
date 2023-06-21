from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from django.urls import include, path, re_path
from users.forms import LoginForm
from users.views import terms_and_conditions_view,complete_google_oauth2
# from blog.views import PostListView,about, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
     
    path('admin/', admin.site.urls),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    

    path('', include('users.urls')),
    path('home/', include('home.urls')),
    

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    
#     path('blog', PostListView.as_view(), name='blog-home'),
#     path('user/<str:username>', UserPostListView.as_view(), name='blog-posts'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
#     path('post/new/', PostCreateView.as_view(), name='blog-create'),
#     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
#     path('about/', about, name='blog-about'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('auth/', include('social_django.urls', namespace='social')),
     path('auth/complete/google-oauth2/', complete_google_oauth2, name='google_oauth2_complete'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
