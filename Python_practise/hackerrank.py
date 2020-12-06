# set operation
'''
n= int(input())
a=set(input().split())
y=int(input())
b=set(input().split())
print(len(a.union(b)))
'''

n= int(input())
if n%2!=0:
    print("Wierd")
elif n%2==0:
    if n>2 and n<5:
        print("Not Wierd")
    elif n>=6 and n <= 20:
        print("Wierd")
    elif n>20:
        print("Not Wierd")