from main.models import Restaurant,City,RestaurantReview,Dish,DishReview
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from main.serializers import RestaurantModelSerializer,UserModelSerializer, CityModelSerializer
@api_view(['GET'])
@csrf_exempt
def current_user(request):
    serializer = UserModelSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def rest_list(request, format=None):
    if request.method == 'GET':
        rests = Restaurant.objects.all()
        serializer = RestaurantModelSerializer(rests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RestaurantModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def rest_detail(request, pk):
    try:
        rest = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantModelSerializer(rest)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RestaurantModelSerializer(instance=rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
@csrf_exempt
def current_user(request):
    serializer = UserModelSerializer(request.user)
    return Response(serializer.data)