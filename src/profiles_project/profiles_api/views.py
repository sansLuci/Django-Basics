from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
	""""""

	def get(self, request, format=None):
		"""Returns a list of APIView fratures"""

		features = [
			'Uses HTTP methods as function (get, post, put, patch, delete)',
			'It is similar to a traditional Django view',
			'Gives you the most control over your logic',
			'Is mapped manually to the URLs'
		]

		return Response({'message':'Hello', 'features':features}) # passing a dictionary for json output