from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # as_view() is a method which renders the class based view
    # dynamic syntax is used here - int:pk expects a integer primary key from database
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),
]
