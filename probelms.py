# write a program to display a persons name,age and
#address in three different lines 

name='shashank '
age=36
address='INDIA'
print(name)
print (age)
print (address)

#detailed method

name='shashank '
age=36
address='INDIA'
print('name of the person',name)
print ('age of the person',age)
print ('address of the person',address)

# program to swap 2 variable
a= 10
b= 20
a,b=b,a
print('value of a is',a)
print('value of b is',b)

# convert a float into int

a=10.6
print('type of a is ',type(a))
a=(int(a))
print('type of a is',type(a))

# take a detail from students

name=input('enter your name ')
age= input(int('age of student '))
grade=input('enter you grade')
print(name,age,grade)

#create a list of 10 numbers and find out the odd even numbers from it 

# METHOD-1

numbers = [23, 16, 9, 42, 87, 5, 30, 11, 8, 55]
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)  

# Print the results
print("Original list of numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# METHOD-2
N=[1,4,3,6,8,9]
for i in N:
    if i%2 == 0 :
        print(i,"is even number")
    else :
        print(i,'is odd number')

#METHOD-3 (FILTERING METHOD)

N=(1,4,3,6,8,9)
even_numbers =tuple(filter(lambda x: x % 2 == 0, N))
odd_numbers = tuple(filter(lambda x: x % 2 != 0, N))

print("Original list of numbers:", N)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# FIND THE VOWELS FROM A GIVEN STRING

string= "violet"
vowels=['a','e','i','o','u']

for i in string:
    if i in vowels:
        print(i,'is a vowel')
    else :
        print(i,'is not vowel')


#Find out common letters between two strings Using Python

def common_letters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = set1.intersection(set2)
    return common

str1 = 'shashank'
str2 = 'sha'
common_letters = common_letters(str1, str2)
print(common_letters)

