from django.urls import path
from . import views


app_name = "contact_manager"

urlpatterns = [
    path("", views.HomeBaseView.as_view(), name="home"),
    path("add/", views.AddContactView.as_view(), name="add"),
    path("all/", views.AllContactView.as_view(), name="all"),
    path("<int:pk>/edit/", views.EditContactView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeleteContactView.as_view(), name="delete"),
    path("search/", views.search, name="search"),
    path("export/", views.export, name="export"),
]
