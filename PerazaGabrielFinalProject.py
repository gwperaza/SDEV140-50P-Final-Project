"""

Author:  Gabriel Peraza
Date written: 12/3/2024-12/13/2024
Assignment:   Module 08 Final Project
Short Desc:   Simulates Ordering Ice Cream

This program is designed to allow the user to simulate ordering an ice cream cone including different
flavor, cone, and topping options.

First, the user is prompted for a name. This serves no other purpose than to be shown at the end when the
program generates a receipt.

Next, the user will be prompted to choose an ice cream flavor. Choosing a flavor will advance to the next
screen, and the option and it's price will be recorded within variables.

Then, the user will choose a cone. There will be three options, each with their own prices. Once again, 
the chosen item and it's price will be stored in variables.

Finally, the user will be prompted to pick from a variety of toppings. They can proceed without choosing 
any, or they can choose up to three. These values will once again be recorded.

Once the user is finished ordering, the program will generate a receipt including the name of the 
business, the user's name, the individual items the user ordered, the final price of the custom ice cream
cone, the tax amount, and the total price including both the price of the ice cream and the tax.

Pseudocode form:

VARIABLE SETUP:
orderDictionary = empty
orderPrice = 0
orderTax = 0
orderTotal = 0

customerName = Prompt user to input their name

ICE CREAM FLAVOR ORDER:
Ask user to choose an ice cream flavor
record flavor and price in orderDictionary
add value of price to orderPrice
advance state

CONE ORDER:
Ask user to choose a cone type
record cone and price in orderDictionary
add value of price to orderPrice
advance state

TOPPING ORDER:
After option is chosen:
  record topping and price in orderDictionary
  add value of price to orderPrice
wait until user selects 'Finalize Order'
generate and display receipt

ADVANCE STATE:
When advance state received:
  change prompt text
  change image
  change button text
  if state is ice cream flavor:
    advance to cone order
  else
    advance to topping order
    add button to finish order

DISPLAY RECEIPT:
orderTax = 7% of orderPrice
orderTotal = orderPrice = orderTax
add orderTax and orderTotal to orderDictionary
display "Syntax Sweets"
display customerName
display all recorded variables in orderDictionary
ask user if they want to order again

  
"""


# Import that allow for simple GUI development
from breezypythongui import EasyFrame

# While decently diverse, breezypythongui does not supply enough functions for the purposes of
# this project so some regular tkinter imports are necessary for a complete project.
from  tkinter import PhotoImage
import tkinter as tk

# Main body of the GUI setup
class SyntaxSweets(EasyFrame):

    def __init__(self):
        
        # Sets up the initial window of our program, including it's name, size, and background color
        EasyFrame.__init__(self, title = "Syntax Sweets", width = 500, height = 300)
        self.setResizable(False)
        self.setBackground("light pink")

        # Initializes a new variable that will be used to calculate the tax amount at the end of the
        # program, where it will be displayed to the user inside of the receipt.
        self.TAX_AMOUNT = 0.07

        # Initializes a label. Starting out it will simply display that this is the final project,
        # but it will be reutilized several times throughout the project to display different messages
        # to the user.
        self.textMessage = self.addLabel("SDEV140 50P FINAL PROJECT", 0, 0, columnspan = 3, sticky = "N")
        
        #Sets color and font size settings for the above text label.
        self.textMessage["background"] = "light pink"
        self.textMessage["foreground"] = "white"
        self.textMessage["font"] = 50

        # Initializes a second label and it's respective text settings. 
        # This one will not be changed, and will instead remain at the bottom left corner of the screen 
        # at all times simply for cosmetic purposes.
        self.companyName = self.addLabel("SYNTAX SWEETS", 2, 0, sticky = "WS")
        self.companyName["background"] = "light pink"
        self.companyName["foreground"] = "white"

        # Initializes a status variable to the first necessary status setting, which is the choosing of
        # the ice cream flavor. This variable will be reference several times so that the program can
        # track what page the user is currently on at any given moment.
        self.status = "pickIceCream"

        # Sets up an empty dictionary. This dictionary will be added to every time the user orders something.
        # This is to be used at the end of the program, where the dictionary will dispense all of the data
        # contained within to the receipt to be shown to the user.
        self.iceCreamOrder = {}

        # Every time the user orders an item, it will be added to this variable. The reason for storing this
        # information here instead of in the dictionary is so that it can be used for calculations when it's
        # time to generate the tax and total price.
        self.orderPrice = 0

       # Text label that informs the user what the text field below it is for, which is for them to enter
       # their name. Also incudes the color and fontsize settings for this particular label.
        self.nameText = self.addLabel("Please enter your name:", 1, 0, columnspan = 3, sticky = "N")
        self.nameText["background"] = "light pink"
        self.nameText["foreground"] = "white"
        self.nameText["font"] = 50

        # The actual text field in which the user will be entering their name. This value is stored now
        # to be used at the end on the receipt.
        self.inputName = self.addTextField(text = "", row = 1, column = 0, columnspan = 3, sticky = "S")

        # Adds a button prompt for the user to press when they are ready to start ordering. More on this
        # at the checkField function below.
        self.button1 = self.addButton("Start Ordering", 2, 0, columnspan = 3, command = self.checkField)

        # Adds another button that triggers a prompt that closes the program. Once again, more on this
        # when we get to the exit function.
        self.exitButton = self.addButton("Quit", 2, 2, command = self.exit)
    
    # Input validation for the "name" input field. The function runs a check to verify that the input
    # has a value and it contains only letter characters.
    def checkField(self):
      if self.inputName.getText().isalpha() == False:
          # If the program discovers that the input does not meet these conditions, the text color of
          # the label above the input field is changed to red, and displays a message telling the user
          # why their input did not go through.
          self.nameText["foreground"] = "red"
          self.nameText.config(text = "Name is required and must be alphabetical.")
      else:
          # Otherwise, if the input checks out, the user's name is recorded in the iceCreamOrder dictionary
          # and the program continues as normal.
          self.iceCreamOrder["NAME"] = self.inputName.getText()
          self.placeOrder()

    # This function activates once the user has clicked the button to start their order with a valid
    # name input, signifying that the program can now move onto the actual ordering section.
    def placeOrder(self):
        
        # The first thing that happens once the program reaches the ordering state is that everything that
        # has a function in the opening menu is removed, allowing for brand new buttons and functions.
        self.button1.destroy()
        self.inputName.destroy()
        self.nameText.destroy()


        # Changes the text of the top center label, filling it with directions for the user.
        # It now informs the user that they are choosing an ice cream flavor.
        self.textMessage.config(text = "Pick your flavor of ice cream.")

        # Sets up an image to be viewed in the top right of the screen. First it sets up some alternative
        # text, and then imports an image from the file 'flavor.png' to associate with the text.
        self.iceCreamImage = self.addLabel("Digital Art of a scoop of Ice Cream", 0, 2, columnspan = 3, sticky = "N")
        self.image = PhotoImage(file = "flavor.png")
        self.iceCreamImage["image"] = self.image

        # Three additional buttons are added to the scene. The idea is to keep the buttons the same, only 
        # changing the text associated as needed every time the user moves to a different section of the
        # program.

        # For this first stage, the inital text for the buttons is set up now with the names of the ice
        # cream flavors, as this is what the first stage of the program handles.

        self.order1 = self.addButton("Chocolate + $5.00", 1, 0, command = self.option1Chosen)
        self.order2 = self.addButton("Vanilla + $5.00", 1, 1, command = self.option2Chosen)
        self.order3 = self.addButton("Strawberry + $5.00", 1, 2, command = self.option3Chosen)

    # Since the buttons are to remain the same, a system must be built so that the correct functions occur
    # every time the button is pressed. For every button, a check is made to see which state the program
    # is in, and then tells the program which function to perform based on that value.

    # After the status check, the button will submit an item to the iceCreamOrder dictionary, as well as
    # adding a float value of the item's price to the orderPrice variable. As stated, the items and
    # values that get sent depend on which phase the button detects the program to be in.


    # The last thing the button does is activate the function updateOrder to advance the program to the
    # next stage with every button press.
    def option1Chosen(self):
        if self.status == "pickIceCream":
          self.iceCreamOrder["CHOCOLATE SCOOP"] = "$5.00"
          self.orderPrice += 5.00
        elif self.status == "pickConeType":
          self.iceCreamOrder["CAKE CONE"] = "$1.50"
          self.orderPrice += 1.50
        else:
          self.iceCreamOrder["SPRINKLES"] = "$0.10"
          self.orderPrice += 0.10
          self.order1["state"] = "disabled"
        self.updateOrder()
        
    # The same process for button1 is repeated for buttons 2 and 3, only rewritten to include the various
    # values that these buttons are intended to hold.
    def option2Chosen(self):
        if self.status == "pickIceCream":
          self.iceCreamOrder["VANILLA SCOOP"] = "$5.00"
          self.orderPrice += 5.00
        elif self.status == "pickConeType":
          self.iceCreamOrder["SUGAR CONE"] = "$2.00"
          self.orderPrice += 2.00
        else:
          self.iceCreamOrder["FUDGE TOPPING"] = "$0.50"
          self.orderPrice += 0.50
          self.order2["state"] = "disabled"
        self.updateOrder()

    def option3Chosen(self):
        if self.status  == "pickIceCream":
          self.iceCreamOrder["STRAWBERRY SCOOP"] = "$5.00"
          self.orderPrice += 5.00
        elif self.status == "pickConeType":
          self.iceCreamOrder["WAFFLE CONE"] = "$2.50"
          self.orderPrice += 2.50
        else:
          self.iceCreamOrder["NUTS TOPPING"] = "$0.25"
          self.orderPrice += 0.25
          self.order3["state"] = "disabled"
        self.updateOrder()
    
    def updateOrder(self):

      # First, the update order function runs a check to see if the status is pickIceCream, the first 
      # status that gets used in the program.
      if self.status == "pickIceCream":

        # If this check succeeds and this is indeed the status of the program, then this function will 
        # update the status to pickConeType, the next one in the program. Additionally, the function 
        # updates the top center label text again to reflect the change in what the user is ordering, this
        # time the cone type. Lastly, a new image and alternative text are associated with the image
        # variable in order to match the change.
        self.status = "pickConeType"
        self.textMessage.config(text = "Pick your cone type.")
        self.order1.config(text = "Cake Cone + $1.50")
        self.order2.config(text = "Sugar Cone + $2.00")
        self.order3.config(text = "Waffle Cone + $2.50")
        self.iceCreamImage.config(text = "Digital Art of an Ice Cream Cone")
        self.image = PhotoImage(file = "cone.png")
        self.iceCreamImage["image"] = self.image
      elif self.status == "pickConeType":

        # If the initial check fails, the program will run a secondary check to see if the status was
        # already set to order a cone, and updating the status should instead set the program into
        # topping ordering mode. If this is the case, the same process for the change to the cone status
        # occurs, with differences to the text label, buttons, and image.
        self.status = "pickToppings"
        self.textMessage.config(text = "Pick your toppings.")
        self.order1.config(text = "Sprinkles + $0.10")
        self.order2.config(text = "Fudge = $0.50")
        self.order3.config(text = "Nuts + 0.25")
        self.iceCreamImage.config(text = "Digital Art of Ice Cream with Fudge, Sprinkles, and Nuts")
        self.image = PhotoImage(file = "toppings.png")
        self.iceCreamImage["image"] = self.image

        # In contrast to the initial state change, however, this one incudes the initialization of a new
        # button. This is because unlike the previous states, this final state should not end after
        # the user chooses an option. Instead, the user should be able to choose as many or as few toppings
        # as they so please before pressing this button to submit the order.
        self.finalizeOrder = self.addButton("Finalize Order", 2, 1, command = self.generateReceipt)

        # No 'else' statement is used as if the state does not match either pickIceCream or pickConeType,
        # then the program is already at the final state, and should not update if a button is pressed.

    # Finally, once the user has finished ordering their ice cream cone and has chosen to finalize their
    # order, the generateReceipt function is called. In this function, we'll be getting the next page 
    # ready as well as calculating ang generating the receipt window.

    def generateReceipt(self):
       
       # First, the buttons used for ordering are removed, as there is nothing left to order since
       # the program has reached it's end.
       self.order1.destroy()
       self.order2.destroy()
       self.order3.destroy()

       # The image is also removed, as there is no associated image to go with the end of the program.
       self.iceCreamImage.destroy()

       # The top center text label can still be used to communicate with the user, so here we change the
       # value of this text label to indicate that the program is over.
       self.textMessage.config(text = "FINISHED")

       # For a sense of immersion, a new text label is added in the center to inform the user that their
       # order has went through. Of course, seeing as this is a simulation, no order is actually submitted
       # anywhere.
       self.finalText = self.addLabel("Order placed. Thank you!", 1, 1)

       # The proceeding are the text and color settings for the new label.
       self.finalText["background"] = "light pink"
       self.finalText["foreground"] = "white"
       self.finalText["font"] = 50

       # A new button is added for the player to choose if they so wish to start another order.
       self.finalizeOrder.config(text = "Place Another Order", command = self.restart)

       # Now, the setup for the order finished page is complete, and we can start working on generating 
       # the receipt. The first thing that has to happen is the calculation of the tax and order totals
       # so that we can show these values within the receipt.

       # Since we already declared the TAX_AMOUNT constant earlier in the program, all we have to do
       # is multiply the item price gathered throughout the program by the TAX_AMOUNT constant.
       self.orderTax = self.orderPrice*self.TAX_AMOUNT

       # Gathering the order's total is simple. All that needs to happen is the combination of both the
       # item and tax price for the ice cream cone.
       self.orderTotal = self.orderPrice + self.orderTax

       # Now that everything price-related within the program is complete, we can add these values to the
       # iceCreamOrder dictionary so that they can be shown inside of the receipt.

       # For the price entry alone, three '\n's are added to the beginning so that a gap is created
       # between the items ordered and the final price. This is done for both cosmetic pleasure, but also
       # to increase the readability of the receipt. The price will be seperate from the rest of the
       # receipt, making it easier for the user to find this particular value.
       self.iceCreamOrder["\n\n\nPRICE"] = ("$" + str(self.orderPrice))

       self.iceCreamOrder["TAX"] = ("$" + str(round(self.orderTax, 2)))
       self.iceCreamOrder["TOTAL"] = ("$" + str(format(self.orderTotal, ".2f")))

       # A new window is created to hold the receipt. This one must be created with regular tkinter and
       # not breezypythongui, as breezypythongui was used for the main window and does not support
       # multiple windows.
       Receipt = tk.Tk()
       
       #The title of the window and the size are the first things to be set.
       Receipt.title("Receipt")
       Receipt.geometry("200x500")

       # Next, a text field is set up to contain the text of the receipt
       receipt_text = tk.Text(Receipt)
       receipt_text.pack(expand=True, fill="both")

       # Then, before we insert the dictionary we'd been defining throughout the program, we'll go ahead
       # and add the company name to the top of the page.
       receipt_text.insert(tk.END, "SYNTAX SWEETS\n\n\n")

       # Now it's time to add the dictionary. Every key and value held within is printed, with double
       # spacing after each value is written.
       for (key, value) in self.iceCreamOrder.items():
        receipt_text.insert(tk.END, f"{key}: {value}\n\n")

       # After every value has been written, we'll add one final note to the end of the receipt, a simple
       # 'Thank You' message. 
       receipt_text.insert(tk.END, "\nTHANK YOU!")
       
       #Finally, we'll set the text object's state to disabled so that the user cannot write in it.
       receipt_text.config(state="disabled")

    # If the user chooses the button to create a new order, some values have to be reset so that the
    # program continues to functino properly.  
    def restart(self):
       
       # First we need to get rid of the new objects meant only for the last page of the program.
       self.finalizeOrder.destroy()
       self.finalText.destroy()

       # Now, the order price needs to be set back to zero, otherwise starting a new order would
       # add onto the price of the previous one.
       self.orderPrice = 0

       # Next, we set the status back to pickIceCream, so that the buttons function properly, and send
       # the correct values.
       self.status = "pickIceCream"

       # Then, we reset the order dictionary. Without this, the second receipt will contain items from the
       # first one despite them not being ordered the second time around.
       self.iceCreamOrder = {"NAME":self.inputName.getText()}

       # Now everything is set up, and we can trigger the placeOrder function, sending the user back to 
       # the ice cream selection page.
       self.placeOrder()
    
    # This is the exit button's code. Unfortunately, this is the one single part of the program I was
    # never able to figure out. No matter what method I try, whenever the program closes, it always
    # reopens immediately. I was not able to find any information online about why this might be, so I've
    # chalked it up to an inconsistency with breezypythongui that might be causing this issue.
    def exit(self):
       SyntaxSweets().destroy()
  
# Finally is the calling of the SyntaxSweets loop, which initializes the entire program and sets it all
# into motion.
SyntaxSweets().mainloop()