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

'''


i=3
while i>0:
    num= int(input("Guess: "))
    if num==9:
        print("You win!")
        break
    i=i-1
if num!=9:
    print("sorry you failed")