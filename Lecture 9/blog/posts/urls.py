from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]

# localhost:8000/posts/29

# cart
# checkout