from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')
router.register('profile',views.UserProfileViewSet)
## Here basename is not present because this ViewSet already has a Query set assigned to it in the class. 
## We have to provide basename attribute only when either QuerySet is unavailable or we want to override the name of QuerySet.
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),

]