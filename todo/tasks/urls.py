from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('update_task.html/<str:pk>',views.updateTask,name="update_task"),
    path('delete.html/<str:pk>',views.deleteTask,name="delete"),
]