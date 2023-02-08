from django.urls import path
from .views import main_page,edit_todo,delete_todo,check_todo,uncheck_todo,register_user
urlpatterns=[
    path("",main_page,name="main-page"),
    path("edit/<str:pk>/",edit_todo,name='edit-todo'),
    path("delete/<str:pk>/",delete_todo,name="delete-todo"),
    path("check/<str:pk>/",check_todo,name="check-todo"),
    path("uncheck/<str:pk>/",uncheck_todo,name="uncheck-todo"),
    path("register/",register_user,name='register'),
]
