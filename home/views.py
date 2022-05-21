from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework.authentication import TokenAuthentication


# class based view
from rest_framework.views import APIView

# viewset
from rest_framework import status, viewsets

# action
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
# Create your views here.

# ------------Function Based View ------------

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Working',
            'method_called': 'You called GET Method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes Working',
            'method_called': 'You called POST Method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Yes Working',
            'method_called': 'You called PATCH Method'
        })
    else:
        return Response({
            'status': 400,
            'message': 'Yes Working',
            'method_called': 'You called invalid Method'
        })


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'status': True,
        'message': 'To Do List',
        'data': serializer.data

    })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Todo Created',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'fields invalid',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Some Thing Went Wrong',
    })


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is invalid',
                'data': {}
            })
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'invalid uid',
        'data': {}
    })

# ------------Function Based View Ended ------------


# ------------Class Based View ------------


# class based view
class TodoView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = ([IsAuthenticated])
    def get(self, request):
        print(request.user)
        todo_objs = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todo_objs, many=True)
        return Response({
            'status': True,
            'message': 'To Do List',
            'data': serializer.data
        })

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Todo Created',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'fields invalid',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Some Thing Went Wrong',
        })


# ------------Class Based View Ended------------


# ------------Default Router------------


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer  = TimingTodoSerializer(objs, many=True)
        return Response({
                    'status': True,
                    'message': 'Todo feached',
                    'data': serializer.data
                })        
    @action(detail=False, methods=['POST'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Todo Created',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'fields invalid',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Some Thing Went Wrong',
        })
