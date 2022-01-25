from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from subs.models import Subscription, City
from .serializers import SubsSerializer, CitySerializer

# Create your views here.
@permission_classes((IsAuthenticated,))
class SubsAPIView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubsSerializer

@permission_classes((IsAuthenticated,))
class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def city_create(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def city_update(request,pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(instance=city, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def city_delete(request,pk):
    city = City.objects.get(id=pk)
    city.delete()
    return Response('Deleted')




