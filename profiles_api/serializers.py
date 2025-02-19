from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem, GenericModel

class HelloSerializer(serializers.Serializer):
    """ Sample Serializer"""
    name = serializers.CharField(max_length=10)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "email", "name", "password",)
        extra_kwargs={
            'password': {
                "write_only":True,
                "style": {
                    "input_type":"password"
                }
            }
        }


    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
    


class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = ('user_profile', 'status_txt', 'created_on')
        extra_kwargs={
            'user_profile':{
                'read_only':True
            }
        }

class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericModel
        fields = '__all__'
