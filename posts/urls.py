from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewset, PostViewSet


router = SimpleRouter()
router.register('users', UserViewset, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls





#from .views import PostList, PostDetail, UserList, UserDetail


# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]