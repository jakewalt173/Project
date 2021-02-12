""" Simulates a person ordering food at Chipotle.
"""

class Burrito:
    """ Simulates a person ordering food at Chipotle
    
    Attributes:
        name(str): the person ordering
    """
    
    def __init__(self, name):
        """ Initializes the customer object and set the name attribute to the
         name  
        
        Args:
            name (str): the customer name
        
        Side effects:
            Initializes self.name
        """
        self.name = name
        self.ingredients = []
        
    def dietary(self, type1 = None ):
        """ Finds out what dietary bowl the customer wants and inputs it
        into their bowl.
        
        Args:
            type (str): type of base ingredients
        """
        
        keto_salad_bowl = ["lettuce", "steak",
                            "red chili salsa", "cheese", "guacamole"]
        vegan_bowl = ["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce"]
        vegetarian_bowl = ["lettuce", "brown rice", 
                           "black beans", "fajitas", 
                           "tomato salsa","guacamole"]
        if type1 == "keto":
            self.ingredients += keto_salad_bowl
        elif type1 == "vegan":
            self.ingredients += vegan_bowl
        elif type1 == "vegetarian":
            self.ingredients += vegetarian_bowl
        else:
            self.ingredients += self.assemble()
    
    def assemble (self):
        ingredients = []
        base = input("brown rice, white rice, or lettuce? ")
        ingredients.append(base)
        beans = input("pinto or black beans? ")
        ingredients.append(beans)
        protein = input("chicken, steak, carnitas, sofritas (vegan),"
                        "veggies (vegan), barbacoa? ")
        ingredients += protein
        salsa = input("red chili salsa, tomatillo salsa, corn salsa,"
                       " green chili salsa? ")
        salsa = salsa.strip().split(",")
        ingredients += salsa
        toppings = input("cheese, lettuce, sour cream? ")
        toppings = toppings.strip().split(",")
        ingredients += toppings  
        return ingredients
        
    def calories_count(self):
        """ Determines the number of calories per order
        
        Return (int): 
            return the calories count
        """ 
        calorie_list = {'chicken': 180,'steak': 150, 'barbacoa': 170,
                        'carnitas': 210,'sofritas': 150,'fajitas': 20,
                         'white rice': 210, 'brown rice': 210,
                         'black beans': 130,'pinto': 130,'guacamole': 230,
                         'tomato salsa': 25,'corn salsa': 80,
                         'green chili salsa': 15,
                         'red chili salsa': 30,'sour cream': 110,
                         'fajita': 20,'cheese': 110,'lettuce': 5,
                         'queso blanco': 120}
        
        calorie_total = 0
        for i in self.ingredients:
            if i in calorie_list:
                calorie_total += calorie_list[i]
        
        return calorie_total
                
    def price_cal(self):
        """ Determines the price of the customer order
        
        Return (int): 
            return the price of the order 
        """
        prices = {"chicken" : 7.70, "steak" : 8.70 , "barbacoa" : 8.70, 
                "carnitas" : 8.20, "sofritas" : 7.70, "veggie" : 7.70}
        
        price = 0
        for i in self.ingredients:
            if i in prices:
                price += prices[i]
        
        return price
    
    def extra(self, extras = None):
        """ updates self.order price based on extras ordered 
    
        Args:
            extras (lst of str): toppings that are being added extra
        
        Returns:
            total price calculation including the value of the extra toppings
        """
        extra_price = {'chicken': 2.80, 'steak': 3.55, 'barbacoa': 3.55,
                   'carnitas': 3.00, 'sofritas': 2.80, "guacamole" : 2.30, 
                   "queso blanco" : 1.30}
        price = self.price_cal()
        
        if extras != None:
            for i in extras:
                self.ingredients.append(i)
                if i in extra_price:
                    price += extra_price[i]
            return price
        else:
            return None
      
class Bowl(Burrito):
    """class for a burrito bowl order if selected.
    """
    def tortilla(self, option):
        """ Find whether the customer is getting a tortilla on the side
        
        Args (str): 
            customer indicates yes or no
        
        Return (Boolean): 
            whether true of false  
        """
        return option == 'yes'

def customer_pref(type1):
    """ Identifies whether the customer wants a bowl or burrito.
        
    Args:
        type (str): determines whether the customer wants a bowl or burrito 
                
    """
    try:
        if type1 == "bowl" or type1 == "burrito":
            return type1
    except TypeError:
        pass
    
def main():
    name = input("welcome to chipotle! what is your name? ")
    order = input("burrito or bowl? ")
    pref = customer_pref(order)
    if pref == 'bowl':
        chip_order = Bowl(name)
        tort = input("did you want a tortilla on the side? (yes or no): ")
        tor = chip_order.tortilla(tort)
    if pref == 'burrito':
        chip_order = Burrito(name)
    diet = input("do you have any dietary restrictions?"
                 " (keto, vegan, vegetarian, None): ")    
    chip_order.dietary(diet)
    extras = input("did you want any extra toppings? "
                   "(chicken, steak, barbacoa, carnitas, sofritas, guacamole, "
                   "queso blanco): ")
    extras = extras.strip().split(",")
    price = chip_order.extra(extras)
    cals = chip_order.calories_count()
    if chip_order == Bowl:
        print(f'{name}, the total for your bowl will be ${price} and {cals}' 
              f' calories total was there a tortilla on the side? {tor}')
    else: 
        print(f'{name}, the total for your burrito will be ${price} and {cals}' 
              f' calories total')
    
if __name__ == "__main__":
    main()