from rest_framework import serializers
from AcmApp.models import Members, Officers, Events, Comments

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'name', 'email', 'password', 'major', 'graduation_time', 'photo', 'resume')

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officers
        fields = ('id', 'email', 'bio', 'position', 'responsibility')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'name', 'scheduled_date_time', 'host', 'sponsor', 'rsvp')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'content', 'email', 'resume')

    