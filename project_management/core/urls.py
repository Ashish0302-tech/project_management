from django.urls import path
from . import views

urlpatterns = [
    # Client URLs
    path('clients/', views.client_list_create, name='client-list-create'),  # List and Create
    path('clients/<int:pk>/', views.client_detail, name='client-detail'),   # Retrieve, Update, Delete

    # Project URLs
    path('projects/', views.project_list_create, name='project-list-create'),  # List and Create
    path('projects/assigned/', views.projects_assigned_to_user, name='projects-assigned'),  # Projects assigned to the logged-in user
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),  # Retrieve, Update, Delete
]
