"""
URL configuration for ticket_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from support.views import AdminRegister,UserRegister,LogoutView,TicketCreateListView,TicektRetrieveUpdateDelete,StaffAssignView,TicketCommentCreateList,CommentRetrieveUpdateDelete
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/admin/',AdminRegister.as_view()),
    path('api/register/user/',UserRegister.as_view()),
    path('api/login/',ObtainAuthToken.as_view()),
    path('api/logout/',LogoutView.as_view()),

    path('api/ticket/',TicketCreateListView.as_view()),
    path('api/ticket/<int:pk>/',TicektRetrieveUpdateDelete.as_view()),

    path("api/tickets/<int:id>/update/",StaffAssignView.as_view()),

    path('api/ticket/<int:id>/comment/',TicketCommentCreateList.as_view()),
    path('api/comment/<int:pk>/',CommentRetrieveUpdateDelete.as_view()),







    
]
