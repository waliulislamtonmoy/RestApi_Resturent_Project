from rest_framework.serializers import ModelSerializer
from App_Account.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name",
                  "last_name", "mobile", "address"]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

        def create(self, validated_data):
            user = User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                mobile=validated_data['mobile'],
                address=validated_data['address']
            )
            extra_kwargs = {
                'password': {
                    'write_only': True,
                    'style': {'input_type': 'password'}
                }
            }

            return user
