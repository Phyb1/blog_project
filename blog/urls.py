from django.urls import path
from .views import BlogListView, BlogDetail, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns = [
    path('',BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog'),
    path('new_blog/', BlogCreateView.as_view(), name='new_blog'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]