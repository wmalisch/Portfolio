from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs,name='all_blogs'),
    # If there is an integer after blog/, then pass it to the detail function as parameter blog_id
    path('<int:blog_id>/', views.detail, name='detail'),
]
