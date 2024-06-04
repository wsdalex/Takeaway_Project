from lib.restaurant import *
from unittest.mock import Mock
def test_restaurant_is_created_with_order():
    restaurant = Restaurant()
    assert restaurant.order == []

def test_add_menu_item():
    restaurant = Restaurant()
    food = Mock()
    food.name = 'toast'
    food.price = 1.00
    restaurant.add_menu_item(food)
    assert restaurant.menu[0].name == 'toast'
    assert restaurant.menu[0].price == 1.00

def test_display_menu():
    restaurant = Restaurant()
    food = Mock()
    food.name = 'toast'
    food.price = 1.00
    restaurant.add_menu_item(food)
    assert restaurant.display_menu() == '1. toast £1.00 '

def test_add_to_order():
    restaurant = Restaurant()
    food = Mock()
    food.name = 'toast'
    food.price = 1.00
    restaurant.add_menu_item(food)
    restaurant.add_to_order(1)
    assert restaurant.order[0] == food
    assert restaurant.display_order() == '1. toast £1.00 '

def test_complete_order():
    restaurant = Restaurant()
    food = Mock()
    food2 = Mock()
    food.name = 'toast'
    food2.name = 'toast with eggs'
    food.price = 1.00
    food2.price = 2.50
    restaurant.add_menu_item(food)
    restaurant.add_menu_item(food2)
    restaurant.add_to_order(1)
    restaurant.add_to_order(2)
    assert restaurant.complete_order() == '1. toast £1.00 2. toast with eggs £2.50 Total: £3.50'

def test_sending_email():
    restaurant = Restaurant()
    requestor = Mock()
    response = Mock()
    requestor.post.return_value = response
    response.ok = True
    assert restaurant.send_confirmation_email(requestor).ok == True