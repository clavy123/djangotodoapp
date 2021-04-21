from . import views
from django.urls import path
urlpatterns = [
    path('',views.todo,name="todo"),
    path('update/<str:pk>/',views.update,name="update"),
    path('delete/<str:pk>/',views.delete,name="delete"),
    
]
