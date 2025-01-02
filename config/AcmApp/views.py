from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from AcmApp.models import Members, Officers, Events, Comments
from AcmApp.serializers import MemberSerializer, OfficerSerializer, EventSerializer, CommentSerializer


# Create your views here.

class MemberViewset(ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(
        detail=True,
        methods=["POST"],
        parser_classes=[FileUploadParser],
        url_path=r"image/(?P<filename>[a-zA-Z0-9_]+\.jpg)",
    )
    def upload_image(self, request, **kwargs):
        member = self.get_object()

        if "file" not in request.data:
            raise ValidationError("There is no file in the HTTP body.")

        file = request.data["file"]
        member.photo.save(file.name, file)
        return Response(MemberSerializer(member).data)
    
    @action(
        detail=True,
        methods=["POST"],
        parser_classes=[FileUploadParser],
        url_path=r"resume/(?P<filename>[a-zA-Z0-9_]+\.pdf)",
    )
    def upload_resume(self, request, **kwargs):
        member = self.get_object()

        if "file" not in request.data:
            raise ValidationError("There is no file in the HTTP body.")

        file = request.data["file"]
        member.resume.save(file.name, file)
        return Response(MemberSerializer(member).data)


class OfficerViewset(ModelViewSet):
    queryset = Officers.objects.all()
    serializer_class = OfficerSerializer
    
class EventViewset(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class CommentViewset(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer





