"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
 
from accounts.api.views import UserViewSet, GroupViewSet
from comments.api.views import CommentViewSet
 

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/users',  UserViewSet,  basename="user")
router.register(r'api/groups', GroupViewSet, basename='group')

router.register(r'api/comments', CommentViewSet, basename='comments')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #@ https://www.django-rest-framework.org/tutorial/quickstart/
    path('',          include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
