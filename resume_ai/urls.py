from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("logout/", views.logout, name="logout"),
    path("upload-resume/", views.upload_resume, name="upload_resume"),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    path(
    "admin-dashboard/",
    views.admin_dashboard,
    name="admin_dashboard"),
    path("result/<int:id>/", views.result, name="result"),
    path("history/", views.history, name="history"),
    path("profile/", views.profile, name="profile"),
    path(
    "edit-profile/",
    views.edit_profile,
    name="edit_profile",),
    path("contact/", views.contact, name="contact"),
    path(
    "forgot-password/",
    views.forgot_password,
    name="forgot_password"),
path(
    "change-password/",
    views.change_password,
    name="change_password"),
    path("download-report/<int:id>/", views.download_report, name="download_report"),
path(
    "delete-resume/<int:id>/",
    views.delete_resume,
    name="delete_resume",
),
path(
    "history/export/csv/",
    views.export_csv,
    name="export_csv",
),

path(
    "history/export/excel/",
    views.export_excel,
    name="export_excel",
),
path(
    "analytics/",
    views.analytics,
    name="analytics",
),
path(
    "manage-users/",
    views.manage_users,
    name="manage_users",
),

path(
    "manage-resume/",
    views.manage_resume,
    name="manage_resume",
),

path(
    "contact-messages/",
    views.contact_messages,
    name="contact_messages",
),

path(
    "admin-analytics/",
    views.admin_analytics,
    name="admin_analytics",
),

path(
    "delete-message/<int:id>/",
    views.delete_message,
    name="delete_message",
    ),

path(
    "admin-login/",
    views.admin_login,
    name="admin_login",
),

path(
    "admin-logout/",
    views.admin_logout,
    name="admin_logout",
),

path(
    "view-user/<int:id>/",
    views.view_user,
    name="view_user",
),

path(
    "edit-user/<int:id>/",
    views.edit_user,
    name="edit_user",
),

path(
    "delete-user/<int:id>/",
    views.delete_user,
    name="delete_user",
),
path(
    "delete-resume-admin/<int:id>/",
    views.delete_resume_admin,
    name="delete_resume_admin",
),
path(
    "toggle-admin/<int:id>/",
    views.toggle_admin,
    name="toggle_admin",
),
path(
    "admin-export-excel/",
    views.admin_export_excel,
    name="admin_export_excel",
),

path(
    "admin-export-pdf/",
    views.admin_export_pdf,
    name="admin_export_pdf",
),
    path("debug-admin/", views.debug_admin),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    
handler404 = "resume.views.error_404"
handler500 = "resume.views.error_500"