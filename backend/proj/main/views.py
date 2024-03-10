from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Helper
from .serializers import CustomerSerializer, HelperSerializer
from drf_spectacular.utils import extend_schema

class CustomerListView(APIView):
    """
    View for listing all customers or creating a new customer.
    """
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
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
        helpers = Helper.objects.all()
        serializer = HelperSerializer(helpers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HelperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
