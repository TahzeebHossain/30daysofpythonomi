#dictionary practice

'''Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries'''

#Create an empty dictionary called dog
dog = {}
print(type(dog))

#add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Chopper"
dog["color"] = "brown"
dog["breed"] = "Bangladeshi Local"
dog["legs"] = 4
dog["age"] = 3
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name":"Tahjeeb","last_name":"Hossain Chowdhury","gender":"Male","age":32,"marital_status":"Single","skills":["Python","Sql","fast learning","data science","statistics"],"Country":"Bangladesh","City":"Dhaka","address":"47, Rojoni Chowdhury Road, Gendaria, Dhaka-1204"}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print(type(skills))

#Modify the skills values by adding one or two skills
student["skills"].append("Staying Alive")
student["skills"].append("Being Depressed")

print(student["skills"])

#Get the dictionary keys as a list
student_keys = list(student.keys())
print(student_keys)

#Get the dictionary values as a list
student_values = list(student.values())
print(student_values)

#Change the dictionary to a list of tuples using items() method
student_tp = list(student.items())
print(student_tp)

#Delete one of the dictionaries
del student