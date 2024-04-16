from django.urls import path
from .views import add_moviechart,show_moviechart,update_moviechart,delete_moviechart
urlpatterns = [
    path('add/',add_moviechart,name='add_url'),
    path('show/',show_moviechart,name='show_url'),
    path('update/<int:pk>/',update_moviechart,name='update_url'),
    path('delete/<int:pk>/',delete_moviechart,name='delete_url')
]