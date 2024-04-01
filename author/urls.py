from django.urls import path
from .views import AuthorListView, AuthorDetailView


urlpatterns = [
    path("authors/", AuthorListView.as_view(), name="manage-list"),
    path(
        "authors/<int:pk>/",
        AuthorDetailView.as_view(),
        name="manage-detail"
    ),
]

app_name = "author"
