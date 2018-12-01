from django.forms import ModelForm
from .models import Restaurant,City,Dish, Review, RestaurantReview,DishReview


class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		fields=('name','number','telephone','city','user')
			
				
