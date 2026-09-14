from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView
from support.serializers import AdminSerializers,UserSeriaizers,TicketSerializer,TicketCommentSerializer
from rest_framework import permissions,authentication
from rest_framework.views import APIView
from support.models import Ticket,TicketComment
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models import Q
# Create your views here.
class UserRegister(CreateAPIView):
    serializer_class=UserSeriaizers

class AdminRegister(CreateAPIView):
    serializer_class=AdminSerializers

class LogoutView(APIView):
    def post(self,request):
        request.auth.delete()
        return Response({"msg":"Logout Successfully"})
    

class TicketCreateListView(CreateAPIView,ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=TicketSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        tickets=Ticket.objects.filter(created_by=self.request.user)

        status=self.request.query_params.get("status")
        priority=self.request.query_params.get("priority")
        category = self.request.query_params.get("category")

        if status:
            tickets = tickets.filter(status=status)

        if priority:
            tickets = tickets.filter(priority=priority)

        if category:
            tickets = tickets.filter(category=category)

        
        search=self.request.query_params.get("search")

        if search:
            tickets = tickets.filter(
                Q(title__icontains=search) |Q(description__icontains=search)
            )

        
        ordering = self.request.query_params.get("ordering")

        if ordering in [
            "priority",
            "-priority",
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at"
        ]:
            tickets = tickets.order_by(ordering)

        return tickets




class TicektRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=TicketSerializer
    
    queryset=Ticket.objects.all()


class StaffAssignView(UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


    
class TicketCommentCreateList(CreateAPIView, ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketCommentSerializer

    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket, id= self.kwargs.get("ticket"))

        serializer.save(created_by=self.request.user,ticket=ticket)

    def get_queryset(self):
        ticket_id = self.kwargs.get("ticket")

        return TicketComment.objects.filter(ticket_id=ticket_id)

    # def get(self,request,id):
    #     ticket=get_object_or_404(Ticket,id=id)
    #     comments=TicketComment.objects.filter(ticket=ticket)
    #     serializer_instance=TicketCommentSerializer(comments,many=True)
    #     return Response(serializer_instance.data)
    
    # def post(self,request,id):
    #     ticket=get_object_or_404(Ticket,id=id)

    #     serializer_instance=TicketCommentSerializer(data=request.data)

    #     if serializer_instance.is_valid():
    #         serializer_instance.save(ticket=ticket,user=request.user)
    #         return Response(serializer_instance.data)
        
    #     return Response(serializer_instance.errors)

class CommentRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class=TicketCommentSerializer
    queryset=TicketComment.objects.all()

