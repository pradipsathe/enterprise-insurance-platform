from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from .models import Policy, CustomerPolicy
from .serializers import PolicySerializer, PurchasePolicySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import IsCustomer

class PolicyListAPIView(generics.ListAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "policy_type"]
    search_fields = ["title"]
    
class PolicyCreateAPIView(generics.CreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class PolicyUpdateAPIView(generics.UpdateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class PolicyDeleteAPIView(generics.DestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class PurchasePolicyAPIView(generics.CreateAPIView):
    queryset = CustomerPolicy.objects.all()
    serializer_class = PurchasePolicySerializer
    permission_classes = [IsAuthenticated, IsCustomer]