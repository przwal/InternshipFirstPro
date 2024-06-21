from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import PeopleSerializer, CategorySerializer, BlogSerializer, RegisterSerializer, LoginSerializer
from .models import Person,Category,Blog
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])

        if not user:
            return Response({
                'status': False,
                'message': 'Invalid Credentails',
            }, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'status': True, 'message': 'user logged in', 'token': str(token)}, status.HTTP_200_OK)
        

class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({'status': True, 'message': 'user created'}, status.HTTP_200_OK)


# Create your views here.

@api_view(['GET' , 'POST', 'PUT'])
def index(request):
    person = {
        'name' : 'prajjwal',
        'age' : '25',
        'hobbies' : ['music', 'sports', 'coding']
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print("YOU HIT A GET METHOD")
        return Response(person)
    elif request.method == 'POST':
        data = request.data
        print('************')
        print(data['age'])
        print('************')
        print('YOU HIT A POST METHOD')
        return Response(person)
    elif request.method == 'PUT':
        print('YOU HIT A PUT METHOD')
        return Response(person)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def people(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])    
        obj.delete()
        return Response({'message': 'person deleted'})

@api_view(['GET', 'POST'])
def create_category(request):
    if request.method == "GET":
        objs = Category.objects.all()
        serializer = CategorySerializer(objs, many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Respose(serializer.errors)

@api_view(['GET','POST','PATCH'])
def create_blog(request):
    if request.method == "GET":
        objs = Blog.objects.all()
        serializer = BlogSerializer(objs, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = BlogSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET'])
def get_blog_from_category(request, category_id):
    if request.method == "GET":
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found'}, status=404)

        blogs = Blog.objects.filter(blogCategory=category)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    






