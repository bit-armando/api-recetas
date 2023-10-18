from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import viewsets
from blogs.models import Blog
from .serializers import BlogSerializers

from django.contrib.auth import get_user_model

User = get_user_model()


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def list(self, request):
        """
        The list method handles the retrieval of all blog posts.
        """
        queryset = Blog.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """
        The retrieve method retrieves a specific blog post by its primary key.
        """
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        The update method updates an existing blog post using the PUT HTTP method.
        """
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        The destroy method deletes a specific blog post using the DELETE HTTP method.
        """
        instance = self.get_object(pk)
        instance.delete()
        return Response({"message": "Blog post deleted successfully"}, status=204)

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND