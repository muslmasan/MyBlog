from django.urls import path
from . import views
urlpatterns=[
    path('',views.Post_list.as_view(),name='post_list'),
    path('post/create/',views.Create_Post.as_view(),name='post_create'),
    path('delete/<int:pk>/',views.Delete_Post.as_view(),name='post_delete'),
    path('post/<int:pk>/',views.Post_detail.as_view(),name='post_detail'),
    path('update/<int:pk>/',views.Update_post.as_view(),name='post_update'),
    path('author/',views.Author_view.as_view(),name='author'),
]