from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rockapi.models import Type

class TypeView(ViewSet):
    """Rock API types view"""

    def list(self, request):
        
        types = Type.objects.all()
        serialized = TypeSerializer(types, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        rock_type = Type.objects.get(pk=pk)
        serialized = TypeSerializer(rock_type)
        return Response(serialized.data, status=status.HTTP_200_OK)


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'label',)