from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# AbstractBaseUser: it is the base of the djano user model
# PermissionsMixin: Allows us to add permission to our user

# Create your models here.

class UserProfileManager(BaseUserManager):
	"""Helps django to work with our custom user model"""

	def create_user(self, email, name, password=None):
		"""Create a new user profile object"""

		if not email:
			raise ValueError('User must have an email address.')

		email = self.normalize_email(email) # Convert the email to lower case
		user = self.model(email=email, name=name,)

		user.set_password(password) # encrypt the password by saving in hash format
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Making a standard user(created by 'create_user') a superuser"""

		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db) 

		return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Represent a user profile inside our system"""

	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Used to get a user's full name"""

		return self.name

	def get_short_name(self):
		"""Used to get users short name"""

		return self.name

	def __str__(self):
		"""Convert the object into string"""

		return self.email
