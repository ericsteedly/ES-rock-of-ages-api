from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rockapi.models import Rock, Type
from django.contrib.auth.models import User

class RockView(ViewSet):

    def create(self, request):

        return Response("", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def list(self, request):

        try:
            rocks = Rock.objects.all()
            serialized = RockSerializer(rocks, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)




class RockTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('label',)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')



class RockSerializer(serializers.ModelSerializer):

    type = RockTypeSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Rock
        fields = ('id', 'name', 'weight', 'user', 'type',)

