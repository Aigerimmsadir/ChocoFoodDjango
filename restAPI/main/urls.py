from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login_jwt/', obtain_jwt_token),
    path('rest_list/', views.rest_list),
    path('rest_detail/<int:pk>', views.rest_detail),
    path('rest_list_cbv/', views.RestaurantList.as_view()),
    path('rest_detail_cbv/<int:pk>', views.RestaurantDetail.as_view()),
    path('dish_list_cbv/', views.DishList.as_view()),
    path('dish_detail_cbv/<int:pk>', views.DishDetail.as_view()),
    path('login/', views.login),
    path('register/',views.UserCreate.as_view()),
    path('rest_review_list_cbv/',views.RestaurantReviewList.as_view()),
    path('current_user/',views.current_user),
    path('rest_review_detail_cbv/<int:pk>',views.RestaurantReviewDetail.as_view()),
    path('dish_review_list_cbv/', views.DishReviewList.as_view()),
    path('dish_review_detail_cbv/<int:pk>', views.DishReviewDetail.as_view()),
    path('order_list_cbv/', views.OrderList.as_view()),
    path('order_detail_cbv/<int:pk>', views.OrderDetail.as_view()),

]

