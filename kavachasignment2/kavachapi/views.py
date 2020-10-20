from kavachapi.models import Test
from kavachapi.serializers import KavachApiSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class TestList(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        testdata=Test.objects.all()
        serializer = KavachApiSerializer(testdata, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = KavachApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)