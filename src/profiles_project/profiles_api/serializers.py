"""A serializer object is an object in the Django rest framework that 
	we can use to describe the data that we need to return and retrieve from our API.

	It basically converts a text string of JSON to a Python object and vice versa.
"""

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
	"""Serializes a name field."""

	name = serializers.CharField(max_length=10)