size = int(input("Enter the size of the pattern: "))
num = 1
while num <= size:
    for number in range(1,size+1):
        print("*", end="")
    print()
    num += 1
