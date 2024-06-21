from user.views import index, people, create_category, create_blog, get_blog_from_category, RegisterAPI, LoginAPI
from django.urls import path, include

urlpatterns = [
    path('index/', index),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('people/', people),
    path('createCat/',create_category),
    path('createBlog/',create_blog),
    path('getBlogFromCategory/<int:category_id>/', get_blog_from_category),
]
