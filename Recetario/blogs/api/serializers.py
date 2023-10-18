from rest_framework import serializers

from django.contrib.auth import get_user_model
from blogs.models import Blog
from usuarios.api.serializers import CustomUserSerializer
User = get_user_model()


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
            author_info = CustomUserSerializer(source='author', read_only=True)
            model = Blog
            fields = ('title','content', 'author')
