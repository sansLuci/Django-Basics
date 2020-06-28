from django.shortcuts import render
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

