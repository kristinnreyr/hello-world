n = int(input("Enter the length of the sequence: ")) # Do not change this line

sum = 0
a = 1
b = 2
c = 3

for i in range(1, n+1):
    if i == 1:
        print(i)
        continue
    elif i == 2:
        print(i)
        continue
    elif i == 3:
        print(i)
        continue
    sum = (a + b + c)
    a = b
    b = c
    c = sum
    print(sum)