#conditionals

'''Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3'''

'''#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.'''

user_age = int(input("Please enter your age: "))

if user_age >= 18:
    print(f"You are {user_age} and you are old enough to drive")
else:
    years_left = 18-user_age
    print(f"You need to wait {years_left} to learn to drive ")




#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = int(input("I am entering my age: "))
your_age =int(input("Please enter your age: "))

if my_age > your_age:
    print("Hah, still a babe I see, go now run along, play with your plastic dolls")
elif my_age == your_age:
    print("brooooooooooooo")
else:
    print("Sorry sir, did not recognize you without your walking stick, do you need me to help you cross the road?")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

input_a = int(input("Enter a number: "))
input_b = int(input("Another number : "))

if input_a > input_b:
    print("a is greater than b")
elif input_b < input_a:
    print("b is greater than a")
else:
    print("It seems both are equal but let's be honest b can never be a")