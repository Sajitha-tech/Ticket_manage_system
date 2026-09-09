from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from support.serializers import AdminSerializers,UserSeriaizers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class UserRegister(CreateAPIView):
    serializer_class=UserSeriaizers

class AdminRegister(CreateAPIView):
    serializer_class=AdminSerializers

class LogoutView(APIView):
    def post(self,request):
        request.auth.delete()
        return Response({"msg":"Logout Successfully"})
