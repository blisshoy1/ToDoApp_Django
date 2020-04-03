from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('addtodo/', views.addtodo,name='addtodo'),
    path('deletetodo/<int:d_id>/',views.deletetodo),
]
