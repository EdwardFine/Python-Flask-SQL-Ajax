for x in range(151): # Needs to go to 151 instead of 150 because when it equals 150, it will end the loop
    print(x)

for x in range(5,1005,5):
    print(x)

for x in range(1,101):
    if x % 5==0:
        message = "Coding"
        if x % 10==0:
            message += " Dojo"
        print(message)
    else:
        print(x)

sum=0
for i in range(1,500000,2):
    sum += i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum =2
highNum =9
mult =3

for i in range(lowNum+1,highNum+1,mult):
    print(i)
