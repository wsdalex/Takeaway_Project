from lib.food import *

def test_food_created():
    food = Food('toast', 1.00)
    assert food.name == 'toast'
    assert food.price == 1.00