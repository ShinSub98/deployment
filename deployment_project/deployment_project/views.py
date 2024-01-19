from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

class Main(APIView):
    def get(self, request):
        res = {"배포" : "성공"}
        return Response(res, status = status.HTTP_200_OK)