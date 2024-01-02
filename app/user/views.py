"""
View for the User API.
"""
from rest_framework import generics

from user.serializers import UserSerializer

# generics.CreateAPIView handles a post request
# designed for creating objects
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

