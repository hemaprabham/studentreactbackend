from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from students.serializer import *
from .models import*
from django.db.models import Q

# Create your views here.
@csrf_exempt
def viewall(request):
    if request.method=="POST":
        studentlist=Student.objects.all()
        serialised_data=StudentSerializer(studentlist,many=True)
        return HttpResponse(json.dumps(serialised_data.data))
    
@csrf_exempt    
def addall(request):
    if request.method=="POST":
        receiveddata=json.loads(request.body)
        print(receiveddata)
        serialisercheck=StudentSerializer(data=receiveddata)
        if serialisercheck.is_valid():
            serialisercheck.save()
            return HttpResponse(json.dumps({"status":"success"})) 
        else:
            return HttpResponse(json.dumps({"status":"failed"}))       
@csrf_exempt
def delete(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"student delete"}))      
@csrf_exempt
def search(request):
    if request.method=="POST":
        receiveddata=json.loads(request.body)
        getadm=receiveddata["admno"]
        data=list(Student.objects.filter(Q(admno__icontains=getadm)).values())
        return HttpResponse(json.dumps(data))          