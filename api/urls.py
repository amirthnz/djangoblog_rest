from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostList.as_view(), name='item-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='item-detail'),
]