n = 4
row = 4

while row > 0:
    s = 1
    while s <= n - row:
        print(" ", end = "")
        s+=1
    k=1
    while k <= 2*row-1:
        print("*", end = "")
        k+=1
    print()
    row-=1

'''row = 4
num = 10

while row > 0:
    col = 1
    while col <= row:
        print(num, end=" ")
        num -= 1
        col += 1
    print()
    row -= 1'''