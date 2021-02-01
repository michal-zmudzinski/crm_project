from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users
# Create your views here.


@api_view(['GET'])
def apiRoot(request):
    api_urls = {
        'List': '/user-list',
        'Detail': '/user-detail/<str:pk>',
        'Create': '/user-create',
        'Update': '/user-update/<str:pk>',
        'Delete': '/user-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def userList(request):
    queryset = Users.objects.filter(isDeleted=False)
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    user = Users.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def userUpdate(request, pk):
    user = Users.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def userDelete(request, pk):
    user = Users.objects.get(id=pk)
    user.isDeleted = True
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
