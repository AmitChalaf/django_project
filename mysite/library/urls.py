from django.urls import path
from .views import libraryApi,libraryViews

urlpatterns = [
    path('api/books/', libraryApi.BookListApi.as_view(), name='booklist'),
    path('api/book/<int:pk>/', libraryApi.BookApi.as_view(), name='book'),
    path('api/author/<int:pk>/', libraryApi.AuthorApi.as_view(), name='author'),
    path('api/authors/', libraryApi.AuthorListApi.as_view(), name='authorlist'),
]
