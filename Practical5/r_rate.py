#For first time it has 84 students, a persona will effect 1.2 person. At 2 range, the students and effected people will all effect 1.2 people. Have a range and find the law
r=1.2
n=84
for i in range(1,6):
    n=n+r*n
    print(n)
print("n = 84*2.2**5")

