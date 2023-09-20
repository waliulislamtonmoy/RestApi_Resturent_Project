from django.shortcuts import render
from rest_framework import parsers
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from App_Order.models import Order, CustomerDetail, Ingredent
from App_Order.serializer import OrderSerializer, CustomerDetailSerializer, IngredentSerializer


class OrderViewsets(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = [parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser]


class CustomerDetailViewset(ModelViewSet):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerDetailSerializer
    parser_classes = [parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser]


class IngredientViewset(ModelViewSet):
    queryset = Ingredent.objects.all()
    serializer_class = IngredentSerializer
    parser_classes = [parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser]
