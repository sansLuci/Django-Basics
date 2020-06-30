"""A serializer object is an object in the Django rest framework that 
	we can use to describe the data that we need to return and retrieve from our API.

	It basically converts a text string of JSON to a Python object and vice versa.
"""

from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field."""

	name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
	"""Serializer class for User profile."""

	class Meta:
		model = models.UserProfile
		fields = ('id','email','name','password')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self, validated_data):
		"""Override the create_user functionality to change the password
		it creates a new user
		"""

		user = models.UserProfile(
			email = validated_data['email'],
			name = validated_data['name']
		)

		user.set_password(validated_data['password'])
		user.save()


		return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.ProfileFeedItem
		fields = ('id','user_profile','status_text','created_on')
		extra_kwargs = {'user_profile':{'read_only':True}}