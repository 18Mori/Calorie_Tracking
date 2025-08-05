from django.shortcuts import render,  redirect, get_object_or_404
from .models import Food
from django.utils import timezone
from django.db.models import Sum
# Create your views here.

def food_list(request):
    today = timezone.now().date()
    food_items = Food.objects.all()
    total_calories = Food.objects.filter(made_at__date=today).aggregate(Sum('calories'))['calories__sum'] or 0
    return render(request, 'food_list.html', {'food_items': food_items, 'total_calories': total_calories, 'today': today})

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            Food.objects.create(name=name, calories=calories)
        return redirect('food_list')
    return render(request, 'add_food.html')

def delete_food(request,food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('food_list')

def reset_calories(request):
    Food.objects.all().delete()
    return redirect('food_list')