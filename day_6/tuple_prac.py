#practicing tuples

'''Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.'''

#Unpack siblings and parents from family_members
family_members = ("Ayon","Omi","Rokshana","Rumi")

siblings =(family_members[0],family_members[1])
parents = (family_members[2],family_members[3])
print(siblings)
print(parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruit = ("Apple","Mango","Banana","tomato")
vegetables = ("Cauliflower","sprouts","Pumpkin","Eggplant","Ladyfinger")
animal_products = ("Milk","Cheese","Curd","castor oil")

food_stuff_tp = tuple(fruit+vegetables+animal_products)
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
n_tp= len(food_stuff_tp)
n_lt= len(food_stuff_lt)
print(n_lt)
print(n_tp)

middle_item_tp = food_stuff_tp[n_tp//2]
middle_item_lt = food_stuff_lt[n_tp//2]

print(middle_item_lt)
print(middle_item_tp)

#Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

'''Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print('Iceland' in nordic_countries)
