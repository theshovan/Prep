n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

print("The array is:", arr)
