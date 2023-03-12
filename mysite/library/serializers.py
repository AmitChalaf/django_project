from rest_framework import serializers
from . import models


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
