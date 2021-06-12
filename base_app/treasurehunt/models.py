from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django import forms
from django.core import validators
from datetime import date

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users Must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        # Not necessary to write anything inside brackets
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom Manager To handle users with email field as the main field
    # instead of username
    objects = UserProfileManager()
    # Done to handle Django Admin
    USERNAME_FIELD = 'email'
    # Required Field can include more fields
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Return String representation of user"""
        return self.name


# Create your models here.
class Score(models.Model):

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    last_answer = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class Answer(models.Model):
    answer = models.CharField(max_length=255)


class AnswerChecker(models.Model):
    index = models.PositiveIntegerField(default=0, unique=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

    def ans_value(self):
        return self.answer