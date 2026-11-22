'''Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard'''
from os import remove

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
n_IT = len(it_companies)
print(n_IT)

#Add 'Twitter' to it_companies
twitter =['twitter']
it_companies.update(twitter)
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["Discord","Netflix","Snapchat"])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("Snapchat")
print(it_companies)

'''Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely'''
#Join A and B
AjoinB=A.union(B)
print(AjoinB)

#Find A intersection B
AintB = A.intersection(B)
print(AintB)

#Is A subset of B
isAofB = A.issubset(B)
print(isAofB)

#Are A and B disjoint sets
AdisjB= A.isdisjoint(B)
print(AdisjB)

#Join A with B and B with A
BjoinA = B.union(A)
print(BjoinA)

#What is the symmetric difference between A and B

AsymdiffB = A.symmetric_difference(B)
print(AsymdiffB)

#Delete the sets completely
del it_companies
del A
del B

'''Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'''


#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(len(age))
print(len(age_st))
#solution: length of the list is bigger than the length of the set as the set only has unique elements

#Explain the difference between the following data types: string, list, tuple and set
#Ans: strings are composites of characters or strings themselves, lists are ordered mutable group of data, tuples are immutable group of data and sets are unordered group of data but they contain only unique values

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
motivation = "I am a teacher and I love to inspire and teach people"
words = motivation.split()
print(words)
uniq_words = set(words)
print(uniq_words)