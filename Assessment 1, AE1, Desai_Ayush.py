#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem One 

temperature = str(input("Please enter temperature "))

#Converts tempature using formula and then rounds it to 3 decimal places
fahrenheitTemp = format(round((float(temperature) * 9/5) + 32, 3), ".3f")
celsiusTemp =  format(round((float(temperature) - 32) * 5/9, 3), ".3f")

#Prints it all together using format
print("{} Celcius is about {} Fahrenheit".format(temperature, fahrenheitTemp))
print("{} Fahrenheit is about {} Celcius".format(temperature,celsiusTemp))


# In[ ]:


#Problem 2

#Asks user what they arithmetic they'd like to do. Is a string so no floats/integers will be valid
userInput = str(input("add/subtract/multiply/divide? "))

numberOne = float(input("Input the first number? "))
numberTwo = float(input("Input the second number? "))
answer = 0
sign = ""

yesNo = input("Would you like to reverse the numbers? (y/n)")

#Reverses numbers depending on if user wants to 
if (yesNo == "y"):
  temp = numberOne
  numberOne = numberTwo
  numberTwo = temp

#Does basic arithmetic 
if (userInput == "add"):
  sign = "+"
  answer = numberOne + numberTwo
elif (userInput == "subtract"):
  sign = "-"
  answer = numberOne - numberTwo
elif (userInput == "multiply"):
  sign = "*"
  answer = numberOne * numberTwo
elif (userInput == "divide"):
  sign = "/"
  answer = numberOne / numberTwo


#Prints final answer
print(str(numberOne) + " " + sign + " "+ str(numberTwo) + " = " + str(answer))


# In[ ]:


#Problem 3 

ageCount = 5
while (ageCount > 0 ):

#Repeats asking user how old they are  
  try:
    ageInput = int(input("How old are you? "))
    if (ageInput >= 0 and ageInput <= 12):
      print ("Child")
    elif (ageInput >= 13 and ageInput <= 19):
      print ("Teenager")
    elif (ageInput >= 20 and ageInput <= 30):
      print ("Young Adult")
    elif (ageInput >= 31 and ageInput <= 64):
      print ("Adult")
    else: 
      print("Senior")
    #Makes it so that the program quits after 5 valid age inputs
    
    ageCount-=1
#If number is not inputed tells user to try again 
  except:
    print("Invalid Entry")


# In[ ]:


##### Problem 4

quit = False

#Creates an empty list that can hold the shopping items 
shoppingItems = []

#Empty list for cost of items
shoppingItemsCost = []
totalCost = 0

#Function to show shopping items beginning with a number and parenthesis 
def show ():
    #Uses zip function to make the two lists parallel one another and print together 
    for items, cost in zip(shoppingItems, shoppingItemsCost):
        print(str(shoppingItems.index(items) + 1) + ") " + str(items) + " $" + str(cost))
        
#Function to clear shopping items out and make empty list 
def clear ():
    shoppingItems.clear()
    shoppingItemsCost.clear()
    
#Function for adding items to shopping cart
def add ():
    addItem = str(input("What would you like to add? "))
    shoppingItems.append(addItem)
    addItemCost = int(input("How much does " + addItem + " cost? "))
    shoppingItemsCost.append(addItemCost)

#While loop for making loop go on forever 

while (quit == False):

    userInput = str(input("quit/add/remove/show/clear: "))
     
    #Sets quit to true and breaks program
    if (userInput == "quit"):
        print("Thanks for using our program. ")
        print("Here is your cart: ")
        show()
        
        #Adds total cost using for loop
        for costOfItem in shoppingItemsCost:
            totalCost += costOfItem
        
        print("Your total is $" + str(totalCost) + " US Dollars ")
            
        quit = True

    #Adds user input into cart
    elif (userInput == "add"):
        add()
    
    elif (userInput == "show"):
        show()
    #Removes item from cart
    elif (userInput == "remove"):
        
        #Shows cart and then asks user what they would like to remove, also removes price 
        show()
        deleteItem = int(input("What would you like to remove? Type in the number of the slot "))
        shoppingItems.pop(deleteItem-  1)
        shoppingItemsCost.pop(deleteItem - 1)
        
    #Clears cart
    elif (userInput == "clear"):
        clear()


# In[ ]:





# In[ ]:





# In[ ]:




