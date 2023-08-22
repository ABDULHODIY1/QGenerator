from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',Homeview.as_view(),name="home"),
    path('Create/',CreatePostViews.as_view(),name='create'),
    path('Update/<int:pk>/',UpdatePostViews.as_view(),name='update'),
    path('Detail/<int:pk>/',DetailViews1.as_view(),name='detail'),
    path('Delete/<int:pk>/',Deleteview.as_view(),name='delete'),
    path('show-tests/',TestViews.as_view(),name='test-show'),
    path('accounts/profile/',rel1.as_view() , name='profile'),
    # path('posts/', PostListView.as_view(), name='post-list'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    
    ]

