from django.urls import path, include
from base import views
from django.contrib.auth.views import LogoutView


app_name = 'base'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register_account/', views.RegisterAccount.as_view(), name='register_account'),

    path('', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('create-task/', views.TaskCreate.as_view(), name='create_task'),
    path('edit/<int:pk>', views.TaskUpdate.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', views.TaskDelete.as_view(), name='task-delete'),
]