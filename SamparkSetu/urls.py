from django.urls import path
from . import views

urlpatterns = [
    path('contactus/',views.contactus,name='ss-contactus'),
    path('', views.form, name="form"),
    path('home/', views.home, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
    path('form/', views.form, name='form'),
]