#1 Describe the problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

#2 Design the classes

-Restaurant Class
    -Contains list of food items
    -Ability to add new food items
    -Method to display all menu items
    -Ability to add items to a order
    -Method to complete order and receive receipt plus send text

-Food Class
    -Contains food and price



#3 Create exampples as integration tests

The user creates a new order
restaurant = Restaurant()
assert restaurant.order.items == []

The user adds a new item to the menu
restaurant.add_menu_item('Toast', 3.55)
assert restaurant.display_menu() == '1. Toast £3.55'


The user adds food to the order
restaurant.add(food)
assert restaurant.diaplay_order() == [food]

The user completes order and returns receipt
assert restaurant.complete_order() == 'Itemized receipt'



#4 Create examples as unit tests

The restaurant is created succesfully with a empty order
restaurant = Restaurant()
assert restaurant.order.items == []

The restaurant returns a receipt on request
assert restaurant.complete_order == 'itemized receipt'

The restaurant add a new food item to the menus

The restaurant return the menu correctly
assert restaurant.display_menu() == '1. Toast £3.55'

The user can pick a item and add it to the order
restaurant.add_to_order(3)
assert restaurant.current_order == [food]

The food item is created correctly
food = Food('toas',1.11)
assert food.name == 'toast'
assert food.price == 1.11

The order can have items added
order = Order()
order.add(food)
assert order.items == [food]

The order can have items removed
order.items = [food1, food2]
order.remove(1)
assert order.items == [food2]


#5 Implement behaviour