'''

print('Wilander '*5)

price = 10
rating = 4.9
is_published = False 
name = "Wilander is awesome"
 

if is_published:
    print(name)


# Print patient name, age and whether he is new patient

name = 'Wilander'
age = 32
is_patient = False 


print (name)
print(age)
print(is_patient)


 

name = input('Whats is your name? ' )
lastname = input('Whats your last name? ')
print ('Hi '+name+' '+lastname)

birth_year = int(input('Birth year: '))
age = 2020 - birth_year

print(type(age))
 

weight = input('Enter your weight in lb ')
kg = float(weight)* 0.45
print(kg)


 
#strings , slicing

course = 'Python for beginers'

print(course)
print(course[1:-1])
 
name = 'alisa'
print(name[1:-2])
 
# formatted string
name = 'Wilander'
last = 'Tauro'

msg = f'{name} {last} is an awesome coder'
msg1 = name + ' ' +last + ' is awesome'
print(msg)
print(msg1)
 

name ='Wilander'

print(len(name))

print(name.upper())
print(name)


name = 'Wilander is awesome'
print(name.find('m'))
print(name.replace('Wilander','Alisa'))
print('Wilander' in name)


x= 20
x+=3

print(x)

y = 10 + 3 *2 ** 2
print(y)

z = (2+3) * 10 - 3
print(z)
 

x= 2.9
print(round(x))

 

#import math




is_hot = True 
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
print("Enjoy the weather")



price =1000000
credit_good = True

if credit_good:
    down_payment = price *.10
else:
    down_payment = price *.20
print(f"Down payment: ${down_payment}")


#logical operators

has_high_income= True
has_good_credit = False

if has_high_income and not has_good_credit:
    print("Eligible for loan")
if has_high_income or has_good_credit:
    print("eligble for loan")


#comparison operators

temperature = 30

if temperature>30:
    print("It's hot day")
elif temperature < 30:
    print("Its not hot day")
else:
    print("It's perfect day")


name = input("Enter your name ")

if len(name)<3:
    print("Name must be atleast 3 characters long")
elif len(name)>50:
    print("Name can not be maximum 50 characters")
else:
    print("name looks good")



weight = float(input("enter your weight: "))
lb_kg = input("(L)bs or (K)g: ")


if (lb_kg.lower()=="l"):
    weight*=0.45
    print(f"You are {weight} kg")
elif(lb_kg.lower()=="k"):
    weight/=0.45
    print(f"You are {round(weight)} pounds")

# While loop

i =5
while i>0:
    print('*' * i)
    i-=1
print("Done")


secret_number = 9
guess_count = 0
guess_limit =3
 
while guess_count<guess_limit:
    guess= int(input("Guess: "))
    if guess==secret_number:
        print("You win!")
        break
    guess_count=guess_count+1
else:  
    print("sorry you failed")


command = input("> ")

if command.lower()=="help":
    print("Start - to start the car")
    print("Stop - to stop the car")
    print("quit - to exit")

    option = input("> ")

    if option.lower()=="start":
        print("car started...Ready to go")
    if option.lower()=="stop":
        print("CAr stopped.")
    if option.lower()=="quit":
        exit()
else:
    print("I don't understand that...")
 

### u can also use boolean
command = ""
i=0
j=0
while True:
    command = input("> ").lower()

    if command =="start" and i==0:
        print("car started...Ready to go")
        i=i+1
    elif command =="start" and i>=1:
        print("car is already started")
    elif command =="stop" and j==0:
        print("CAr stopped.")
        i=0
        j+=1
    elif command=="stop" and j>=1:
        print("Car already stopped")
        j=0
    elif command =="help":
        print(""" 
        Start - to start the car
        stop - to stop car
        quit
        
        """)
    elif command =="quit":
        break
    else:
        print("I dont understand")


         

# For loops

for item in 'Python':
    print(item)

for item in range(10):
    print(item)

    

prices = [10,20,30]
sum = 0
for item in prices:
    sum = sum + item
print(sum)
 

for x in range(4):
    for y in range(4):
        print(f'({x},{y})')




numbers = [1,1,1,1,5]

#for number in numbers:
    #print("x"*number) 

for number in numbers:
    output=''
    for count in range(number):
        output+='x'
    print(output)


### how to find maximum number in the list
numbers =[20,10,100,40]
max = numbers[0]
for number in numbers:
    if number > max:
        max= number
print(max)


#Two dimensional list

matrix = [[1,2,3], [4,5,6],[7,8,9]]

print(matrix)
for row in matrix:
    for item in row:
        print(item)
 
 

numbers = [5,3,1,7,4]

numbers.append(10)
print(numbers)

numbers.insert(0,30)
print(numbers)
print(numbers.index(10))
 

numbers.pop()

numbers.clear()


# To remove duplicates from a list
numbers = [10,30,10,20,20]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


## tuple

coordinates = (1,2,3)
x= coordinates[0]
y= coordinates[1]
z= coordinates[2]
x,y,z= coordinates  ## unpacking

print(x)
print(y)
print(z)
 

customer ={
"name":"Wilander"
"age":32


}


phone = input("Enter the phone number ")

ph_dict = { "1":"one","2":"Two","3":"three"}

ph_list =""
for number in phone:

    ph_list+= ph_dict.get(number,"!") +" "
        #print(ph_list)
print(ph_list)



message = input(">")

words= message.split(' ') 

print(words)

emojis= {
":)": "smile",
":(":"sad"

}

output =""

for word in words:
    output+=emojis.get(word, word) + " "

print(output)

#Functions

def greet_user(name):
    print(f"Good Morning {name}")
    print("Welcome aboard")


print("start")
greet_user("Wilander")
print("finish")

def square(side):
    return side*side

print(square(5))

message = input(">")

def emojis_fun(message):
    words = message.split(" ")
    emoji={
        ":)":"smile",
        "(": "sad"
    }
    output=""
    for word in words:
        output+=emoji.get(word,word) + " "
    return output

print(emojis_fun(message))


try:
    age =int(input('Age: '))
    income = 10000
    risk = income/age
    print(age)
except ValueError:
    print("invalid value")
except ZeroDivision: 
    print("age not zero")



class Point:

    def __init__(self, x, y):
        self.x =x
        self.y =y 
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point(10,20)
point1.move()
point1.draw()
#point1.x = 10   ## attributes of point1
#point1.y= 20
print(point1.x)


class Person:

    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


p = Person("wilander")
print(p.name)
p.talk()


class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def annoying(self):
        print ("annoying")

d= Dog()
d.walk()
d.bark()



import converters
print(converters.kgs_to_lbs(50))


from converters import kgs_to_lbs
print(kgs_to_lbs(50))


#3.25.22

from utils import find_maximum

print(find_maximum([12,99,80]))


#import ecommerce.shipping 

#from ecommerce.shipping import calculate_shipping 

from ecommerce import shipping 

shipping.calculate_shipping()


import random

for i in range(3):
    print(random.randint(10,20))

  
## program to roll a dice
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
Dice = Dice()
print(Dice.roll())
  
from pathlib import Path
path = Path('ecommerce')
print(path.exists())


from pathlib import Path
path = Path()

for file in path.glob('*'):
    print(file)

'''

#3.59