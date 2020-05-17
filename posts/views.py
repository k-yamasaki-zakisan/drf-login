from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


#下のクラスをviewsetsで結合
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer






# # ListCreateAPIView -> read-write endpoint
# class PostList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# # RetrieveUpdateDestoryAPIView -> ALlows read, update, delete
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


