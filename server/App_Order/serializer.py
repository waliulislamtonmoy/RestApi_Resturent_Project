from App_Order.models import CustomerDetail, Order, Ingredent
from rest_framework.serializers import ModelSerializer


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = "__all__"


class IngredentSerializer(ModelSerializer):
    class Meta:
        model = Ingredent
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    Ingredents=IngredentSerializer()
    Customers=CustomerDetailSerializer()
    class Meta:
        model = Order
        fields = "__all__"

    def create(self,validated_data):
        Ingredent_Data=validated_data.pop('Ingredents')
        Customer_Data=validated_data.pop('Customers')
        Ingredents=IngredentSerializer.create(IngredentSerializer(),validated_data=Ingredent_Data)
        Customers=CustomerDetailSerializer.create(CustomerDetailSerializer(),validated_data=Customer_Data)

        order,created=Order.objects.update_or_create(
            Ingredents=Ingredents,
            Customers=Customers,
            price=validated_data.pop('price'),
            ordertime=validated_data.pop('ordertime'),
            user=validated_data.pop('user')
        )
        return order

    


