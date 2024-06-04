from lib.restaurant import *
from lib.food import *

def test_add_menu_item():
    restaurant = Restaurant()
    food = Food('toast', 1.00)
    restaurant.add_menu_item(food)
    assert restaurant.menu[0].name == 'toast'
    
def test_display_menu():
    restaurant = Restaurant()
    food = Food('toast', 1.00)
    food2 = Food('toast with eggs', 3.00)
    restaurant.add_menu_item(food)
    restaurant.add_menu_item(food2)
    assert restaurant.display_menu() == '1. toast £1.00 2. toast with eggs £3.00 '

def test_add_food_to_order():
    restaurant = Restaurant()
    food = Food('toast', 1.00)
    food2 = Food('toast with eggs', 3.00)
    food3 = Food('toast with eggs and bacon', 5.50)
    restaurant.add_menu_item(food)
    restaurant.add_menu_item(food2)
    restaurant.add_menu_item(food3)
    restaurant.add_to_order(1)
    restaurant.add_to_order(2)
    restaurant.add_to_order(3)
    assert restaurant.display_order() == '1. toast £1.00 2. toast with eggs £3.00 3. toast with eggs and bacon £5.50 '

def test_return_receipt():
    restaurant = Restaurant()
    food = Food('toast', 1.00)
    food2 = Food('toast with eggs', 3.00)
    food3 = Food('toast with eggs and bacon', 5.50)
    restaurant.add_menu_item(food)
    restaurant.add_menu_item(food2)
    restaurant.add_menu_item(food3)
    restaurant.add_to_order(1)
    restaurant.add_to_order(2)
    assert restaurant.complete_order() == '1. toast £1.00 2. toast with eggs £3.00 Total: £4.00'

