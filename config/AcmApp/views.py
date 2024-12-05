from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from AcmApp.models import Members, Officers, Events, Comments
from AcmApp.serializers import MemberSerializer, OfficerSerializer, EventSerializer, CommentSerializer

# Create your views here.

@csrf_exempt
def memberApi(request,nid = 0):
    if request.method == 'GET':
        members = Members.objects.all()
        members_serializer = MemberSerializer(members, many=True)
        return JsonResponse(members_serializer.data, safe=False)
    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        members_serializer = MemberSerializer(data = member_data)
        if members_serializer.is_valid():
            members_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        member_data = JSONParser().parse(request)
        member = Members.objects.get(id = member_data['id'])
        members_serializer = MemberSerializer(member, data = member_data)
        if members_serializer.is_valid():
            members_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'DELETE':
        member = Members.objects.get(id = nid)
        member.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def officerApi(request,nid = 0):
    if request.method == 'GET':
        officers = Officers.objects.all()
        officers_serializer = OfficerSerializer(officers, many=True)
        return JsonResponse(officers_serializer.data, safe=False)
    elif request.method == 'POST':
        officer_data = JSONParser().parse(request)
        officers_serializer = OfficerSerializer(data = officer_data)
        if officers_serializer.is_valid():
            officers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        officer_data = JSONParser().parse(request)
        officer = Officers.objects.get(id = officer_data['id'])
        officers_serializer = OfficerSerializer(officer, data = officer_data)
        if officers_serializer.is_valid():
            officers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'DELETE':
        officer = Officers.objects.get(id = nid)
        officer.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def eventApi(request,nid = 0):
    if request.method == 'GET':
        events = Events.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
    elif request.method == 'POST':
        event_data = JSONParser().parse(request)
        events_serializer = EventSerializer(data = event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        event_data = JSONParser().parse(request)
        event = Events.objects.get(id = event_data['id'])
        events_serializer = EventSerializer(event, data = event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'DELETE':
        event = Events.objects.get(id = nid)
        event.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def commentApi(request,nid = 0):
    if request.method == 'GET':
        comments = Comments.objects.all()
        comment_serializer = CommentSerializer(comments, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
    elif request.method == 'POST':
        event_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data = event_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        event_data = JSONParser().parse(request)
        event = Comments.objects.get(id = event_data['id'])
        comment_serializer = CommentSerializer(event, data = event_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'DELETE':
        event = Comments.objects.get(id = nid)
        event.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


