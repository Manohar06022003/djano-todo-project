from django.urls import path, include
from todo_app import views 

urlpatterns = [

    path('', views.login_view, name='login'),


    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard_views'),

    # Task operations
    path('add-task/', views.add_task_view, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),

    # Task completion
    path('toggle-task/<int:task_id>/', views.toggle_task_completion_view, name='toggle_task_completion'),

    # Completed and pending tasks
    path('completed-tasks/', views.completed_task_view, name='completed_tasks'),
    path('pending-tasks/', views.pending_task_view, name='pending_tasks'),

]

