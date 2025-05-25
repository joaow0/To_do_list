from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_task, name='create_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
]
