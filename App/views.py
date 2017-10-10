import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from App.models import Schedule, Appuser

@csrf_exempt
def GetSchedule(request):
    data=Schedule.objects.first();
    #user=Appuser.image.url
    user=data.user.image.url;
    msg=data.user.message;
    busy_type=data.user.busyType;
    data=model_to_dict(data);
    data['url']=user;
    data['msg']=msg;
    data['busy_type']=busy_type;
    return HttpResponse(json.dumps(data),content_type="json");
@csrf_exempt
def SaveUserInfo(request):
    user=Appuser(id=1,userId=request.POST['userId'],image=request.FILES['image'],message=request.POST['message']);
    user.save();
    data={};
    data['userId']=user.userId;
    data['image']=user.image.url;
    data['message']=user.message;
    return HttpResponse(json.dumps(data), content_type="json");

@csrf_exempt
def SaveSchedule(request):
    schedule=Schedule.objects.first();
    schedule.name1=request.POST['name1'];
    schedule.name1StartTime=request.POST['name1StartTime'];
    schedule.name1EndTime=request.POST['name1EndTime'];
    schedule.name2=request.POST['name2'];
    schedule.name2StartTime=request.POST['name2StartTime'];
    schedule.name2EndTime=request.POST['name2EndTime'];
    schedule.name3=request.POST['name3'];
    schedule.name3StartTime=request.POST['name3StartTime'];
    schedule.name3EndTime=request.POST['name3EndTime'];



    # Schedule(user=user,name1=request.POST['name1'],name1StartTime=request.FILES['name1StartTime'],
    #               name1EndTime=request.POST['name1EndTime'],name2=request.POST['name2'],name2StartTime=request.FILES['name2StartTime'],name2EndTime=request.POST['name2EndTime'],
    #               name3=request.POST['name3'], name3StartTime=request.POST['name3StartTime'],
    #               name3EndTime=request.FILES['name3EndTime']);
    schedule.save();
    data=model_to_dict(schedule);
    return HttpResponse(json.dumps(data), content_type="json");

@csrf_exempt
def SaveUserMsg(request):
    user=Appuser.objects.first();
    user.message=request.POST["Msg"];
    user.save();
    data={};
    data['userId']=user.userId;
    data['image']=user.image.url;
    data['message']=user.message;
    return HttpResponse(json.dumps(data), content_type="json");

@csrf_exempt
def SaveUserBusy(request):
    user=Appuser.objects.first();
    user.busyType=request.POST["busyType"];
    user.save();
    data={};
    data['userId']=user.userId;
    data['image']=user.image.url;
    data['message']=user.message;
    return HttpResponse(json.dumps(data), content_type="json");