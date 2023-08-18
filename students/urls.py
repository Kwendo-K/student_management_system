"""
student app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_user, name="logout"),
    path("edit_record/<int:pk>", views.edit_record, name="edit_record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
    path("record/<int:pk>", views.view_record, name="record"),
    path("export_csv", views.export_csv, name="export_csv"),
]
