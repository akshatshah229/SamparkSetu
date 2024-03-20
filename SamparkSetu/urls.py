from django.urls import path
from . import views

urlpatterns = [
    path('contactus/',views.contactus,name='ss-contactus'),
    path('', views.FormViewsModel.as_view(), name="form"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
    path('adminuser/', views.adminuser, name="adminuser"),
]