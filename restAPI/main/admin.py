from django.contrib import admin
from .models import Restaurant,City,Dish, Review, RestaurantReview,DishReview,Order,OrderItem
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(City)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)