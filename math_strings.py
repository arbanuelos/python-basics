#Create two variables for two types of fruit you own (integer values).
#Create two variables for their prices (float values).
#Calculate and print:
#Total number of fruits
#Total cost
#Update the fruit counts (simulate eating or buying some).
#Combine your first and last name into one string.
#Print:
#Your name in uppercase
#Your name in lowercase
#The number of characters in your name
pear = 2
watermelon = 1
price_of_pear = 2.00
price_of_watermelon = 5.00
price_combined = price_of_pear + price_of_watermelon
print(pear + watermelon)
#or im not sure so i created another variable that adds the fruit
total_fruit = pear + watermelon
print(total_fruit)
#it works so then the prompt says to update fruit being eaten or added
#so i created varible with the =- and =+ symbol and used to print with total

eats =-1
buys_fruit =+1

print(eats + total_fruit)
#here it is adding fruit to total
print(buys_fruit + total_fruit)

first_name = "Andrew "
last_name ="Banuelos"
name_together  = (first_name + last_name)
print(name_together)
#so i added a space to the end of first name to get the space needed
characters_in_name = 14
print(name_together, characters_in_name)
#<Your name> has <number of fruits> fruits now, worth $<total cost>.
#print(name_together, total_fruit, price_combined) 
#attempting string prompt
print("My name is", name_together,"I have", total_fruit, "Here's the cost", price_combined)