from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem, UserItem
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.hashers import check_password


# Serializer for TodoItem
class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'


# Serializer for UserItem
class UserItemSerializer(ModelSerializer):
    class Meta:
        model = UserItem
        fields = ['userName', 'password']


class TodoListView(APIView):
    renderer_classes = [JSONRenderer]  # Force JSON response, no browsable API

    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)


class UserCreateView(APIView):
    def post(self, request):
      
        username = request.data.get('userName')
        password = request.data.get('password')

    
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    
        user = UserItem(userName=username)
        user.set_password(password)
        user.save()

        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('userName')
        password = request.data.get('password')

       
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserItem.objects.get(userName=username)
        except UserItem.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

      
        if user.check_password(password):
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return HttpResponse("Welcome to the Django API!")
