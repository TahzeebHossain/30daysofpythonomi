#conditional practice

#Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are old enough to drive")
else:
    print(f"You have to wait {18-user_age} years to learn to drive")

'''''Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 
'years' for bigger differences, and a custom text if my_age = your_age.'''

my_age = int(input("I will enter my age: "))
your_age = int(input("Please enter your age: "))

if my_age == your_age:
    print("We are the same age, yay!")
elif my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am one year older than you")
    else:
        print(f"I am {diff} years older than you")
else:
    diff = your_age - my_age
    if diff == 1:
        print("You are one year older than me")
    else:
        print(f"You are {diff} years older than me")

'''Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b,
if a is less b return a is smaller than b, else a is equal to b.'''

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a is equal to b")

#Level 2

'''Write a code which gives grade to students according to theirs scores:'''
'''```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```'''

st_score = int(input("Enter your score to get your grade: "))

if 90 <= st_score <= 100:
    print("Your grade is A")
elif 80 <= st_score <= 89:
    print("Your grade is B")
elif 70 <= st_score <= 79:
    print("Your grade is C")
elif 60 <= st_score <= 69:
    print("Your grade is D")
elif 0 <= st_score <= 59:
    print("Your grade is F")

'''Get the month from user input then check 
if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer'''

autumn_month = ["September", "October","November"]
winter_month = ["December","January","February"]
spring_month = ["March","April","May"]
summer_month = ["June","July","August"]

user_month = input("Enter your month: ")

if user_month in autumn_month:
    print("You are in Autumn season")
elif user_month in winter_month:
    print("You are in Winter season")
elif user_month in spring_month:
    print("You are in Spring season")
elif user_month in summer_month:
    print("You are in Summer season")

'''If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
 If the fruit exists print('That fruit already exist in the list')'''

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter your fruit name: ")

if user_fruit not in fruits:
    fruits.append(user_fruit)
    print(fruits)
else:
    print("That fruit already exists in the list")

'''
* Check if the person dictionary has skills key, 
if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, 
 if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, 
 print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!
 
 * If the person is married and if he lives in Finland, 
 print the information in the following format:
     Asabeneh Yetayeh lives in Finland. He is married.'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

'''* Check if the person dictionary has skills key, 
if so print out the middle skill in the skills list.'''

if "skills" in person:
    print(person["skills"])

''' * Check if the person dictionary has skills key, 
 if so check if the person has 'Python' skill and print out the result.
 '''

if "skills" in person:
    if "Python" in person["skills"]:
        print("Python is in the list")
    else:
        print("python is not in the list")

'''* If a person skills has only JavaScript and React, 
 print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!'''

if "skills" in person:
    skills = person["skills"]

    if "React" in skills and "Node" in skills and "MongoDB" in skills:
        print("He is a fullstack developer")
    elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
        print("He is a backend developer")
    elif set(skills) == {"JavaScript","React"}:
        print("He is a frontend developer")
    else:
        print("Unknown title")



'''* If the person is married and if he lives in Finland, 
 print the information in the following format:
     Asabeneh Yetayeh lives in Finland. He is married.'''

if "country" in person and "is_married" in person:
    if person["country"] == "Finland" and person["is_married"] == True:
        print(f"{person["first_name"]} {person["last_name"]} lives in {person["country"]} and He is married ")