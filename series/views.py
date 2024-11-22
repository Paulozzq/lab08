from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Serie, Category
from rest_framework import viewsets
from .serializers import SerieSerializer, CategorySerializer, LoginSerializer,  UserSerializer

# CRUD para Series
class SeriesView(APIView):
    def get(self, request):
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SerieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SerieDetailView(APIView):

    def get(self, request, serie_id):
        serie = get_object_or_404(Serie, pk=serie_id)
        serializer = SerieSerializer(serie)
        return Response(serializer.data)

    # Actualizar una serie específica
    def put(self, request, serie_id):
        serie = get_object_or_404(Serie, pk=serie_id)
        serializer = SerieSerializer(serie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar una serie específica
    def delete(self, request, serie_id):
        serie = get_object_or_404(Serie, pk=serie_id)
        serie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD para Categorías
class CategoryView(APIView):
    # Obtener todas las categorías
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # Crear una nueva categoría
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    # Obtener detalles de una categoría específica
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # Actualizar una categoría específica
    def put(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar una categoría específica
    def delete(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
