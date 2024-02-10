1.  Print 'True' if a is greater than or equal to 5, 'False' otherwise

num_list = [2, 5, 8, 7, 13, 15]
for i in num_list:
    if i>5 :
        print("true")
    else :
        print("false")
    i+=1
    
2.Take a string input of your name and store it as a list of separate letters.

name=input("enter your name ")
l=list(name)
print(l)

3. for set type

name=input("enter your name ")
l=set(name)
print(l)

4.Print the sum of numbers from 1 to n where n is the input by the user.

n=int(input("enter the number"))
for i in range(1,n):
    n=n+i
print(n)

5. other method is 

n=int(input())
a=int((n*(n+1))/2)
print(a)

6.Print all the even numbers between 1 to n where n is the input given by user.
n=int(input())
for i in range (0,n,2):
   print(i)
   
7.Print all the numbers from n to 1 in reverse order.
n=int(input())
for i in range (n,0,-1):
    print(i)
8.
