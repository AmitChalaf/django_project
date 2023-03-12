from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import generics
from ..models import Author, Book
from ..serializers import AuthorSerializers, BookSerializers

#get,post
class BookListApi(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BookApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializers
    lookup_url_kwarg = 'pk'
    queryset = Book.objects.all()


class AuthorApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializers
    lookup_url_kwarg = 'pk'
    queryset = Author.objects.all()

class AuthorListApi(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    