#Because it will be 13 numebers, a range will have 2 number, so final we should have another a to describe it. A number is the sum of the previous two numbers
a=1
b=1
print(a)
print(b)
for i in range (1,6):
    a=a+b
    print(a)
    b=a+b
    print(b)
a=a+b
print(a)
