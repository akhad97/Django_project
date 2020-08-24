from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),

    path('student_signup/', views.student_signup, name='student_signup'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('teacher_signup/', views.teacher_signup, name='teacher_signup'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='portal/password_reset.html'),
     name='reset_password'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="portal/password_reset_sent.html"), 
        name="password_reset_done"),
    
    

    # path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='portal/password_reset_form.html'),
    #  name='password_reset_confirm'),

    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='portal/password_reset_done.html'),
    #  name='password_reset_complete'),
]