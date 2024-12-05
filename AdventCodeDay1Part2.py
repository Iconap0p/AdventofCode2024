import re
from pathlib import Path

lines = []
with open('/Users/Icona_pop/Desktop/AdventofCode2024/digits.txt', 'r') as file:
    lines = file.readlines() 

left_column=[]
right_column=[]

for line in lines:
    left, right = line.split()
    left_column.append(int(left))
    right_column.append(int(right))
    
left_column_sorted = sorted(left_column)
right_column_sorted = sorted (right_column)

#Count # of times a number appears in a list 
# Loop through the left column 
# Find the number of similarity populates in the right column 
# Multiply the number of similarities by the # of occurences
sum =0
for number in left_column_sorted:
    occurence = right_column_sorted.count(number)
    similarity = occurence * number
    sum = sum+ similarity
    print (number)
    print(occurence)
    print(similarity)

print(sum)
