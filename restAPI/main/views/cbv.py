from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from main.serializers import *
from main.models import Restaurant,Dish,DishReview,RestaurantReview,City
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class RestaurantList(APIView):
    pagination_class = (PageNumberPagination,)
    def get(self, request):
        rests = Restaurant.objects.all()
        serializer = RestaurantModelSerializer(rests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantModelSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(id=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rest = self.get_object(pk)
        serializer = RestaurantModelSerializer(rest)
        return Response(serializer.data)

    def put(self, request, pk):
        rest = self.get_object(pk)
        serializer = RestaurantModelSerializer(instance=rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rest = self.get_object(pk)
        rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DishList(APIView):

    def get(self, request):
        dish = Dish.objects.all()
        serializer = DishModelSerializer(dish, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DishDetail(APIView):

    def get_object(self, pk):
        try:
            return Dish.objects.get(id=pk)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dish = self.get_object(pk)
        serializer = DishModelSerializer(dish)
        return Response(serializer.data)

    def put(self, request, pk):
        dish = self.get_object(pk)
        serializer = DishModelSerializer(instance=dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dish = self.get_object(pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class RestaurantReviewList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        rest_review = RestaurantReview.objects.all()
        serializer = RestaurantReviewModelSerializer(rest_review, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantReviewModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantReviewDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return RestaurantReview.objects.get(id=pk)
        except RestaurantReview.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rest_review = self.get_object(pk)
        serializer = RestaurantReviewModelSerializer(rest_review)
        return Response(serializer.data)

    def put(self, request, pk):
        rest_review = self.get_object(pk)
        serializer = RestaurantReviewModelSerializer(instance=rest_review, data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rest_review = self.get_object(pk)
        rest_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class DishReviewList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        dish_review = DishReview.objects.all()
        serializer = DishReviewModelSerializer(dish_review, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DishReviewModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DishReviewDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return DishReview.objects.get(id=pk)
        except DishReview.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dish_review = self.get_object(pk)
        serializer = DishReviewModelSerializer(dish_review)
        return Response(serializer.data)

    def put(self, request, pk):
        dish_review = self.get_object(pk)
        serializer = DishReviewModelSerializer(instance=dish_review, data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dish_review = self.get_object(pk)
        dish_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class OrderList(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        order = Order.objects.filter(owner = request.user)
        serializer = OrderModelSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = OrderModelSerializer(data=request.data,context={'items': request.data.get('items')})
        if serializer.is_valid():

            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderModelSerializer(order)
        return Response(serializer.data)


    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

