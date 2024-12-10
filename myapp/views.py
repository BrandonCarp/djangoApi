from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoItem
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

class TodoListView(APIView):
    renderer_classes = [JSONRenderer]  # Force JSON response, no browsable API
    
    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)

def home(request):
    return HttpResponse("Welcome to the Django API!")