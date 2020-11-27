# -----------------------------------------------------------------------------
# Define Pants class
# -----------------------------------------------------------------------------
class Pants:
    """
    the Pants class represents an article of clothing sold in a store.
    """
    def __init__(self, color, waist_size, length, price):
        """
        Method for initializing a Pants object.

        Args:
            color (str): Color of a pants object.
            waist_size (int): Waist size of a pants object.
            length (int): Length of a pants object.
            price (float): Price of a pants object.
        """
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
        
    def change_price(self, new_price):
        """
        Method for changing the price of a Pants object.
        
        Args:
            new_price (float): New price of a pants object.
        """
        self.price = new_price
        
    def discount(self, discount):
        """
        Method to calculate and return a discount on a Pants object.
        
        Args:
            discount (float): Discount on a pants object, e.g. 0.05 = 5%.
        """
        return self.price * (1 - discount)

# -----------------------------------------------------------------------------
# Define unit check
# -----------------------------------------------------------------------------
def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12

    pants.change_price(10)
    assert pants.price == 10
    assert pants.discount(.1) == 9
    print('You made it to the end of the check. Nice job!')

# -----------------------------------------------------------------------------
# Perform unit check
# -----------------------------------------------------------------------------
check_results()

# -----------------------------------------------------------------------------
# Define SalesPerson class
# -----------------------------------------------------------------------------
class SalesPerson:
    
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0
        
    def sell_pants(self, pants):
        self.pants_sold.append(pants)
        
    def display_sales(self):
        for i in self.pants_sold:
            print(
                'color: {}, '
                'waist_size: {}, '
                'length: {}, '
                'price: {}'.\
                format(
                    i.color,
                    i.waist_size,
                    i.length,
                    i.price
                )
            )
                
    def calculate_sales(self):
        total_sales = 0
        for i in self.pants_sold:
            total_sales += i.price
        return total_sales
    
    def calculate_commission(self, percentage):
        total_sales = self.calculate_sales()
        return total_sales * percentage

# -----------------------------------------------------------------------------
# Define unit check
# -----------------------------------------------------------------------------
def check_results():

    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    assert salesperson.pants_sold[0] == pants_one
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')

# -----------------------------------------------------------------------------
# Perform unit check
# -----------------------------------------------------------------------------
check_results()
