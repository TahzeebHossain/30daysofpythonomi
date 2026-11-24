#loops level 2 practice

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total+=i

print(f"The sum of 0 to 100 is {total}")

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#even numbers

total_even = 0
total_odd = 0

for i in range(101):
    if i % 2 == 0:
        total_even+=i
    else:
        total_odd+=i

print(f"The sum of all even numbers from 0 to 100 is {total_even}")
print(f"The sum of all even numbers from 0 to 100 is {total_odd}")