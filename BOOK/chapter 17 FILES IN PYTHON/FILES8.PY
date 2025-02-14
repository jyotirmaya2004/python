#Pickle in python
import EMP,pickle

#open emp.dat file as binary file for writting
f=open("emp.wb","w")
n=int(input("How may employees ? "))

for i in range(n):
    id=int(input("Enter a ID : "))
    name=input("Enter your name : ")
    sal=float(input("ENter your salary : "))