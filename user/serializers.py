from rest_framework import serializers
from .models import Person,Category,Blog
from django.contrib.auth.models import User

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('Username is Taken')
        
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('Email is Taken')
        return data

    def create(seld, validated_data):
        user = User.objects.create(username = validated_data['username'] ,email = validated_data['email'])
        user.set_password(validated_data['password'])
        return validated_data
        print(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


