from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name='ss-about'),
    path('', views.home, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
    path('form/', views.form, name='form'),
]