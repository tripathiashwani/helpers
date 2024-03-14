from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Helper
from .serializers import CustomerSerializer, HelperSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import re



class CustomerListView(APIView):
    """
    View for listing all customers or creating a new customer.
    """

    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve the authenticated user
        user = request.user.id
        # print(user,"this is customer call")

        # Filter customers queryset based on the authenticated user
        # customers = Customer.objects.all()
        # print(customers,"customers")
        # Serialize the filtered queryset
        serializer = CustomerSerializer(request.user)
        
        # Return the serialized data
        # print(serializer.data)

        return Response(serializer.data)
    
    permission_classes=[IsAuthenticated]
    def post(self, request):
        user = request.user.id
        print(user,"this is customer call")
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HelperListView(APIView):
    """
    View for listing all helpers or creating a new helper.
    """
    def get(self, request):
        # permission_classes=[IsAuthenticated]
        helpers = Helper.objects.all()
        serializer = HelperSerializer(helpers, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes=[IsAuthenticated]
        print(request.data)
        serializer = HelperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
