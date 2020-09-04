from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('detail/<int:pk>/', views.PipeDetailView.as_view(), name='pipe_detail'),
    path('', views.PipeListView.as_view(), name='pipe_list')
]
