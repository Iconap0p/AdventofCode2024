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
sum = 0
for lefts,rights in zip(left_column_sorted,right_column_sorted):
    differences= abs(lefts - rights)
    sum = sum + differences
    print (differences)
    print(lefts,rights)
print (sum)
