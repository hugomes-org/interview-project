from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .models import MyData
from rest_framework.decorators import api_view

# from .models import MyData
from .serializer import MyDataSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@api_view(['GET'])
def ListAllMyData(request):
    datas = []

    for i in range(30):
        mydata = MyData()
        mydata.value = i**2
        datas.append(mydata)
    serialize = MyDataSerializer(datas,many=True)
    return Response(serialize.data)

@api_view(['GET'])
def GetMyData(request,number):
    return Response(number**2)
    