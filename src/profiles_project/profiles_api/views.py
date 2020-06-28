from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

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



