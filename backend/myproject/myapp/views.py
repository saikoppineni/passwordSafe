from django.shortcuts import render

# Create your views here.
from rest_framework import status,generics
from rest_framework.response import Response

from .models import NoteModel
from .serializers import NoteSerializer

class Notes(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self,request):
        try:
            mainuser1 = request.GET.get('mainuser')
            mainpass1 = request.GET.get('mainpass')
            users = NoteModel.objects.filter(mainuser=mainuser1, mainpass=mainpass1)
            data = []
            for user in users:
                user_data = {
                    'username': user.username,
                    'password': user.password,
                    'description': user.description,
                    }
                data.append(user_data)
            return Response(data)
        except Exception as e:
            return Response(e)
    
    def post(self,request):
        data = request.data
        username1 = data.get('username')
        password1 = data.get('password')
        description1 = data.get('description')
        mainuser1 = data.get('mainuser')
        mainpass1 = data.get('mainpass')
        user = NoteModel(mainuser=mainuser1,mainpass=mainpass1,username=username1, password=password1, description=description1)
        user.save()
        return Response({"success"})

    # def get(self,request):
    #     notes = NoteModel.objects.all()
    #     serializer = self.serializer_class(notes,many=True)
    #     return Response({
    #         "notes":serializer.data,
    #         "message":"this is a message"
    #     })

    # def post(self,request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status":"Success","data":{"note":serializer}})
