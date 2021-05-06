from django.urls import path 
from .views import UserList, PostList
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("user", UserList, basename="user")
router.register("", PostList, basename="post")

urlpatterns = router.urls