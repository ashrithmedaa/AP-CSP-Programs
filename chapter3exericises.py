
#Ashrith Meda Chapter 3 Exercises
#1 
dayNum = int(input("Enter a day number (1-7): "))

if dayNum == 1:
    print("Monday")
elif dayNum == 2:
    print("Tuesday")
elif dayNum == 3:
    print("Wednesday")
elif dayNum == 4:
    print("Thursday")
elif dayNum == 5:
    print("Friday")
elif dayNum == 6:
    print("Saturday")
elif dayNum == 7:
    print("Sunday")
else:
    print("Invalid day number")

#2
rect1_length = float(input("Enter the length of rectangle 1: "))
rect1_width = float(input("Enter the width of rectangle 1: "))
rect2_length = float(input("Enter the length of rectangle 2: "))
rect2_width = float(input("Enter the width of rectangle 2: "))

rect1_area = rect1_length * rect1_width
rect2_area = rect2_length * rect2_width

if rect1_area > rect2_area:
    print("Rectangle 1 has the greater area.")
elif rect2_area > rect1_area:
    print("Rectangle 2 has the greater area.")
else:
    print("Both rectangles have the same area.")

#3
age = int(input("Enter the person's age: "))

if age <= 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is a senior.") #Extra was another key to include senior citizens
else:
    print("The person is an adult.")
#4 

romanNum = int(input("Enter a number between 1 and 10: "))

match romanNum:
    case 1:
        print("I")
    case 2:
        print("II")
    case 3:
        print("III")
    case 4:
        print("IV")
    case 5:
        print("V")
    case 6:
        print("VI")
    case 7:
        print("VII")
    case 8:
        print("VIII")
    case 9:
        print("IX")
    case 10:
        print("X")

#5 

mass = float(input("Enter the mass: "))
weight = mass * 9.8

if weight < 100:
    print("The object is too light.")
if weight > 500:
    print("The object is too heavy.")

#6 

month = int(input("Enter a month number (1-12): "))
day = int(input("Enter a day number (1-31): "))
year = int(input("Enter a year: "))

if(month * day == year):
    print("The date is magic!")
else:
    print("The date is not magic.")

#7

color1 = input("Enter the first primary color: ")
color2 = input("Enter the second primary color: ")

if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("The resulting color is purple.")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("The resulting color is orange.")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("The resulting color is green.")
else:
    print("Error, only enter primary colors.")

#8 

hot_dogs_per_pack = 10
buns_per_package = 8

num_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

total_needed = num_people * hot_dogs_per_person
packages_of_hot_dogs = total_needed // hot_dogs_per_pack
if total_needed % hot_dogs_per_pack != 0:
    packages_of_hot_dogs += 1

total_buns_needed = total_needed
packages_of_hot_dog_buns = total_buns_needed // buns_per_package
if total_buns_needed % buns_per_package != 0:
    packages_of_hot_dog_buns += 1

leftover_hot_dogs = (packages_of_hot_dogs * hot_dogs_per_pack) - total_needed
leftover_hot_dog_buns = (packages_of_hot_dog_buns * buns_per_package) - total_buns_needed
print("The minimum number of packages of hot dogs required:", packages_of_hot_dogs)
print("The minimum number of packages of hot dog buns required:", packages_of_hot_dog_buns)
print("The number of hot dogs that will be left over:", leftover_hot_dogs)
print("The number of hot dog buns that will be left over:", leftover_hot_dog_buns)

#9

rouletteNumber = int(input("Enter a roulette number (0-36): "))

if rouletteNumber == 0:
    print("The number is green.")
if rouletteNumber >= 1 and rouletteNumber <= 10:
    if rouletteNumber % 2 == 0:
        print("The number is black.")
    else:
        print("The number is red.")
    if rouletteNumber >= 11 and rouletteNumber <= 18:
        if rouletteNumber % 2 == 0:
            print("The number is red.")
        else:
            print("The number is black.")
    if rouletteNumber >= 19 and rouletteNumber <= 28:
        if rouletteNumber % 2 == 0:
            print("The number is black.")
        else:
            print("The number is red.")
    if rouletteNumber >= 29 and rouletteNumber <= 36:
        if rouletteNumber % 2 == 0:
            print("The number is red.")
        else:
            print("The number is black.")
else:
    print("Invalid roulette number.")

#10
print("Enter the number of coins to make a dollar:")
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
pennies = int(input("Enter the number of pennies: "))
quarters = int(input("Enter the number of quarters: "))

if (nickels * 5 + dimes * 10 + pennies * 1 + quarters * 25) == 100:
    print("Congratulations! You made a dollar.")
elif (nickels * 5 + dimes * 10 + pennies * 1 + quarters * 25) < 100:
    print("You made less than a dollar.")
else:
    print("You made more than a dollar.")

#11

booksPurchased = int(input("Enter the number of books purchased: "))
if booksPurchased == 0:
    points = 0
elif booksPurchased == 2:
    points = 5
elif booksPurchased == 4:
    points = 15
elif booksPurchased == 6:
    points = 30
elif booksPurchased >= 8:
    points = 60

print("The number of points earned is:", points)

#12 
initialPrice = 99
quantityPurchased = int(input("Enter the quantity purchased: "))
if quantityPurchased < 10:
    discount = 0
elif quantityPurchased >= 10 and quantityPurchased <= 19:
    discount = 0.1
elif quantityPurchased >= 20 and quantityPurchased <= 49:
    discount = 0.2
elif quantityPurchased >= 50 and quantityPurchased <= 99:
    discount = 0.3
elif quantityPurchased >= 100:
    discount = 0.4

print("The total price after discount is:", quantityPurchased * initialPrice * (1 - discount))

#13 

totalWeight = float(input("Enter the total weight of the package in pounds: "))

if totalWeight <= 2:
    shippingCost = 1.50
elif totalWeight <= 6 and totalWeight > 2:
    shippingCost = 3.00
elif totalWeight <= 10 and totalWeight > 6:
    shippingCost = 4.00
elif totalWeight > 10:
    shippingCost = 4.75

print("The shipping cost is:", shippingCost * totalWeight)

#14 

numSeconds = int(input("Enter the number of seconds: "))
seconds = numSeconds % 60
minutes = (numSeconds // 60) % 60
hours = numSeconds // 3600
days = numSeconds // 86400

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

#15(Feburary Project)



