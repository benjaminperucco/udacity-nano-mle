# -----------------------------------------------------------------------------
# import functions from source files
# -----------------------------------------------------------------------------
from shirt import Shirt
from tests import run_tests

# -----------------------------------------------------------------------------
# instantiate a shirt object with the following characteristics:
#   - color red, size S, style long-sleeve, and price 25
# store the object in a variable called shirt_one
# -----------------------------------------------------------------------------
shirt_one = Shirt(
    shirt_color='red',
    shirt_size='S',
    shirt_style='long-sleeve',
    shirt_price=25
)

# -----------------------------------------------------------------------------
# print the price of the shirt using the price attribute
# use the change_price method to change the price of the shirt to 10
# print the price of the shirt using the price attribute
# use the discount method to print the price of the shirt with a 12% discount
# -----------------------------------------------------------------------------
print('Initial price of shirt 1: USD{}'.format(shirt_one.price))
shirt_one.change_price(10)
print('Price of shirt 1 after change: USD{}'.format(shirt_one.price))
print('Discounted price of shirt 1 is: USD{}'.format(shirt_one.discount(.12)))

# -----------------------------------------------------------------------------
# instantiate another object with the following characteristics:
#   - color orange, size L, style short-sleeve, and price 10
# store the object in a variable called shirt_two
# -----------------------------------------------------------------------------
shirt_two = Shirt(
    shirt_color='orange',
    shirt_size='L',
    shirt_style='short-sleeve',
    shirt_price=10
)

# -----------------------------------------------------------------------------
# calculate the total cost of shirt_one and shirt_two
# store the results in a variable called total_price
# -----------------------------------------------------------------------------
total_price = shirt_one.price + shirt_two.price
print('Total price of shirt 1 and shirt 2 is: USD{}'.format(total_price))

# -----------------------------------------------------------------------------
# use the shirt discount method to calculate the total cost if shirt_one has
# a discount of 14% and shirt_two has a discount of 6%
# store the results in a variable called total_discount
# -----------------------------------------------------------------------------
total_discount = shirt_one.discount(.14) + shirt_two.discount(.06)
print('Total discounted price is: USD{}'.format(total_discount))

# -----------------------------------------------------------------------------
# unit tests to check your solution
# -----------------------------------------------------------------------------
run_tests(shirt_one, shirt_two, total_price, total_discount)
