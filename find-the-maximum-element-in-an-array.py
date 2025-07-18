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

ar.sort(reverse=True)

# Method 4: Simply printing the first element of the sorted array in descending order
for i in range(len(ar)):
    if i == 0:
        print("First element of the sorted array in descending order:", ar[i])
        break


# Method 5: Sorting in ascending order without using build-in function and then printing the last element  
ar2 = [3, 17, 2, 10, 8]

for i in range(len(ar2)):
    for j in range(i + 1, len(ar2)):
        if ar2[i] > ar2[j]:           
            # Swapping elements
            ar2[i], ar2[j] = ar2[j], ar2[i]

print("Sorted array in ascending order:", ar2)
print("Last element value:", ar2[len(ar2)-1])

# Method 6: Sorting in descending order without using build-in function and then printing the first element
ar2 = [3, 17, 2, 10, 8]

for i in range(len(ar2)):
    for j in range(i + 1, len(ar2)):
        if ar2[i] < ar2[j]:           
            # Swapping elements
            ar2[i], ar2[j] = ar2[j], ar2[i]

print("Sorted array in descending:", ar2)
print("First element value:", ar2[0])
