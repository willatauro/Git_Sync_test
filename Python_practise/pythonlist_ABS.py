'''
catlist = []

while True:
    print("enter name of cat " + str(len(catlist)+1) + ' Enter nothing  to exit')
    cat = input()

    if cat=='':
        break
    catlist= catlist + [cat]
print("the name of cat are: ")
for i in catlist:
    print(i)

'''
