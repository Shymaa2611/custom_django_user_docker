from rest_framework import serializers
from .models import customuser,Profile

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, max_length=20)

    class Meta:
        model = customuser
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})

        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
       
        user = customuser(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=email
            )
        user.set_password(password)
        user.save()

        return user
        



class ProfileSerializer(serializers.ModelSerializer):
    kid = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()  

    class Meta:
        model = Profile
        fields = ['email', 'kid']

    def get_kid(self, obj):
        user = obj.user
        if user.kid:
            kid_data = {
                'name': user.kid.name,
                'password': user.kid.password if user.kid.password else user.password,
                'access_code': user.kid.access_code
            }
            return kid_data
        else:
            return None

    def get_email(self, obj): 
        return obj.user.email


