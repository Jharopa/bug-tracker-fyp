from django.urls import path

# Bugs app imports.
from . import views

app_name = "bugs"

urlpatterns = [
    path("", views.BugListView.as_view(), name="bug_list"),
    path("create/", views.BugCreateView.as_view(), name="bug_create"),
    path("detail/<int:id>/", views.BugDetailView.as_view(), name="bug_detail"),
    path("update/<int:id>/", views.BugUpdateView.as_view(), name="bug_update"),
    path("delete/<int:id>/", views.BugDeleteView.as_view(), name="bug_delete"),
    path("close/<int:id>/", views.close_bug_view, name="bug_close"),
]
