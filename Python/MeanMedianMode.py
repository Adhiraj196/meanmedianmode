from ast import Str
import csv

from numpy import append
with open('SOCR-HeightWeight.csv', newline= '') as f:
    reader = csv.reader(f)
    filedata = list (reader)
filedata.pop(0)
newdata = []
for i in range(len (filedata)):
    num = filedata[i][1]
    newdata = append(num)

#calculate me
n = len(newdata)
total = 0 
for x in newdata : 
    total += x

mean = total / n 
print("mean is : + str(mean)")