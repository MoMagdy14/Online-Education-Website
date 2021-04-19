from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField


User = get_user_model()

# class LoginSerializers(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password"]
    
class RegisterSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()
    email = serializers.EmailField(max_length=60, required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ["username", "email", "password", "age", "phone","country", "school", "graduation_state", "governorate", "gender", "graduation_year"]
        extra_kwargs = {
            'password': {'write_only': True},
            "id": {"read_only": True},
        }
        