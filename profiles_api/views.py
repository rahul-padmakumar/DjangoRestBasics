from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import HelloSerializer, ProfileSerializer
from .models import UserProfile
from . import permissions

# Create your views here.
class HelloApiView(APIView):
    def get(self, req):
        return Response({"method": "GET"})
    def post(self, req):
        serializer =  HelloSerializer(data=req.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({"method": "POST", "value": name})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, req, pk=None):
        return Response({"method": "PUT"})
    
    def patch(self, req, pk=None):
        return Response({"method": "PATCH"})
    
    def delete(self, req, pk=None):
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """ Class to try out working of viewset """

    serializer_class = HelloSerializer

    def list(self, req):
        """ This function returns list"""
        return Response(
            {
                "message": [
                    "Hello",
                    "I am trying",
                    "ViewSets"
                ],
                "method": "GET"
            }
        )
    
    
    def create(self, req):
        """ function for create"""
        serialized_data = self.serializer_class(data = req.data)
        if serialized_data.is_valid():
            name = serialized_data.validated_data.get("name")
            return Response({"method": "CREATE", "value": name})
        else:
            return Response(
                serialized_data.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, req, pk=None):
        """Function for getting an object"""
        return Response({"method": "Retrieve", "pk": pk})
    
    def update(self, req, pk=None):
        """Functon to update"""
        return Response({"method": "Update"})
    
    def partial_update(self, req, pk=None):
        """Function to try partial_update"""
        return Response({"method": "Partial Update"})
    
    def destroy(self, req, pk=None):
        """Function to try delete"""
        return Response({"method":"Delete"})
    

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
