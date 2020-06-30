from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # HTTP status
from rest_framework.authentication import TokenAuthentication # provide authentication to update own profile
from rest_framework import filters # provide filter for search functionality
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly # Gives permission to do anything if auth else restricts to just read only
from rest_framework.permissions import IsAuthenticated # It only allows when user is authenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloAPIView(APIView):
	""""""

	serializer_class = serializers.HelloSerializer # Storing the serializer into a variable

	def get(self, request, format=None):
		"""Returns a list of APIView fratures"""

		features = [
			'Uses HTTP methods as function (get, post, put, patch, delete)',
			'It is similar to a traditional Django view',
			'Gives you the most control over your logic',
			'Is mapped manually to the URLs'
		]

		return Response({'message':'Hello', 'features':features}) # passing a dictionary for json output


	def post(self, request):
		"""Showing a Hello message with name."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {}'.format(name)
			return Response({'message':message})

		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

	def put(self, request, pk=None):
		"""Update an entry"""

		return Response({'method':'put'})

	def patch(self, request, pk=None):
		"""Partially update, only to specific fields"""

		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		"""Delete an entry"""

		return Response({'method':'delete'})

# Create Viewset classes

class HelloViewset(viewsets.ViewSet):

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a hello message"""

		features = [
			'Uses action (list, create, update, partial update, destroy)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code'
		]

		return Response({'message':'Hello', 'features':features})

	def create(self, request):

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid:
			name = 'Hello {0}!'.format('name')
			message = serializer.data.get(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

	def retrieve(self, request, pk=None):

		return Response({'http_method':'GET'})

	def update(self, request, pk=None):

		return Response({'http_method':'PUT'})

	def partial_update(self, request, pk=None):

		return Response({'http_method':'PATCH'})

	def delete(self, request, pk=None):

		return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handles creating and updating the user profile. In-built class in Django."""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
	"""Checks email and password and returns Auth Token."""

	serializer_class = AuthTokenSerializer

	def create(self, request):
		"""Use the ObtainAuthToken APIView to validate and create a token. """

		return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated,) # IsAuthenticatedOrReadOnly

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)

