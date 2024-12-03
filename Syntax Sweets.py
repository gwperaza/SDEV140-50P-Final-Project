"""

Author:  Gabriel Peraza
Date written: 12/3/2024
Assignment:   Module 08 Final Project
Short Desc:   Simulates Ordering Ice Cream

This program is designed to allow the user to simulate ordering an ice cream cone including different cone and topping options.
First, the user is prompted for a name. This serves no other purpose than to be shown at the end when the prograam generates
a receipt.

Next, the user will be prompted to choose an ice cream flavor. Choosing a flavor will advance to the next window, and the option and
it's price will be recorded within variables.

Then, the user will choose a cone. There will be three options (Cake, Sugar, Waffle) each with their own prices. Once again, the 
chosen item and it's price will be stored in variables.

Finally, the user will be prompted to pick from a variety of toppings. They can proceed without choosing any, or they can choose up 
to three. These values will once again be recorded.

Once the user is finished ordering, the program will generate a receipt including the name of the business, the user's name,
the individual items the user ordered, the final price of the custom ice cream cone, the tax amount, and the total price including both the price 
of the ice cream and the tax.

Pseudocode form:

VARIABLE SETUP:
topping1 = "None"
topping1Price = 0
topping2 = "None"
topping2Price = 0
topping3 = "None"
topping3Price = 0

customerName = Prompt user to input their name

ICE CREAM FLAVOR ORDER:
Ask user to choose an ice cream flavor
record variables iceCreamFlavor, iceCreamPrice

ICE CREAM CONE ORDER:
Ask user to choose a cone type
record variables coneType, conePrice

TOPPING ORDER:
Ask user to choose toppings or proceed without
After option is chosen
while toppings < 3 and choice is not "No additional toppings"
  if topping1 equals "None":
      fill topping1, topping1Price
  elif topping2 = "None":
      fill topping2, topping2Price
  else
    fill topping3, topping3Price

DISPLAY RECEIPT:
display "Syntax Sweets"
display customerName
display variables iceCreamFlavor, iceCreamPrice
display variables coneType, conePrice
If value not "None" or 0:
  display topping1, topping1Price, topping2, topping2Price, topping3, topping3Price
orderPrice = iceCreamPrice + conePrice + topping1Price + topping2Price + topping3Price
display orderPrice
taxPrice = orderPrice*0.07
display taxPrice
totalPrice = orderPrice + taxPrice
display totalPrice 

  
"""

#Import that allow for simple GUI development
from breezypythongui import EasyFrame



class SyntaxSweets(EasyFrame):

 
    #Sets up our GUI
    def __init__(self):
        #Sets up the initial pixel width and height values, as well as the title given
        #to the GUI window.
        EasyFrame.__init__(self, title = "Syntax Sweets", width = 300, height = 150)
        
SyntaxSweets().mainloop()
