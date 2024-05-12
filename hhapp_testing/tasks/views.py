from rest_framework import generics

# возможно потом можно будет убрать.
from rest_framework.response import Response
from rest_framework.views import APIView
# ----
from django.shortcuts import render, HttpResponse
from .models import ResearchRef
from .serializers import ResearchRefSerializer

#Create your views here.
class ResearchRefAPIList(generics.ListCreateAPIView):
    queryset = ResearchRef.objects.all()
    serializer_class = ResearchRefSerializer


def home(request):
    #return HttpResponse('hello world')
    return render(request, 'index.html', context={})


