from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status

from api.serializer import FilmeSerializer,UserSerializer
from api.models import Filme

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListCreateFilme(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = FilmeSerializer(Filme.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['usuario'] = request.user.id  # Associa o usuário logado ao campo 'usuario'
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 



from django.http import Http404

...

class DetailUpdateDeleteFilme(APIView):

    def get_filme(self, pk):
        try:
            return Filme.objects.get(pk=pk)
        except Filme.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        filme = self.get_filme(pk)
        serializer = FilmeSerializer(filme)
        return Response(serializer.data)

    def put(self, request, pk):
        filme = self.get_filme(pk)
        serializer = FilmeSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        filme = self.get_filme(pk)
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from rest_framework.permissions import IsAuthenticated

