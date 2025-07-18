ar = [3, 17, 2, 10, 8]

print(f"Original array list:", ar)

# Method 1: Using the max() function to find the maximum element
print("Maximum element in the array using max() function:", max(ar))

ar.sort(reverse=False)

# Method 2: Simply sorting the array in ascending order and printing the last element ar [-1]
print(f"Last element of array list-sorted in ascending order:", ar[-1])

# Method 3: Simply printing the last element of the sorted array using a loop
for i in range(len(ar)):
    if i == len(ar) -1:
        print("Last element of the sorted array using a loop:", ar[i])
        break

