#print('hello world')


#name = input('please enter your name')
#print(name)

first_name = 'Wilander'
last_name = 'Tauro'

## String 
#first_name = input('Please enter your first name')
#last_name = input('Please enter last name')
#print(first_name.capitalize() +' '+ last_name.capitalize())

# Formatting the string 
#output = 'Hello, ' +first_name +' ' + last_name
#output = 'hello {} {}'.format(first_name,last_name)
#output = f'hello, {first_name} {last_name}'
#print(output)

# Numbers

#first_num = 6
#second_num = 2
#print(first_num+second_num)

#type conversion

#days_in_Feb = 28
#print(str(days_in_Feb) + ' days in feb')

#datatype conversion

# first_num = input('enter first number')
# second_nm = input('enter second numebr')

#print(int(first_num)+int(second_nm))
# print(float(first_num)+float(second_nm))


### Dates 

from datetime import datetime, timedelta 

# current_Date  = datetime.now()

# print('Today is: ' + str(current_Date))

# today = datetime.now()
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print(yesterday)

# print('day'+ str(today.day))

#### convert string to date 

birthday = input('when is your birthday(dd/mm/yyyy)')

birthday_date = datetime.strptime(birthday,'%d/%m/%Y')

print('birthday: '+str(birthday_date))

