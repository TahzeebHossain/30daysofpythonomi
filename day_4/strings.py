my_string = "   Where did you go?   "
full_stripped = my_string.strip()
print(full_stripped)

right_stripped = my_string.rstrip()
print(right_stripped)


left_stripped = my_string.lstrip()
print(left_stripped)

splitter = input("Say something")

formatted_spiller = splitter.split(' ')
print(formatted_spiller)

joiner = (input("Say something: "))

letter_1,letter_2,letter_3,letter_4,letter_5,letter_6 = joiner[0],joiner[1],joiner[2],joiner[3],joiner[4],joiner[5]

print(letter_1) 
print(letter_2) 
print(letter_3) 
print(letter_4) 
print(letter_5) 
print(letter_6) 

print(joiner)

#print(joiner.join())

reunion = join(joiner)
