# Practice while loop

n = 1

while n <= 10:
    if n == 5:
        n += 1
        continue
    # print(n**2)
    print(f"{n}^2 ==> {n**2}")
    n += 1

# Print numbers from 1 to 10 using a while loop.
print("\n ===========================")
n = 1

while n <= 10:
    print(n)
    n += 1

# Print all even numbers between 1 and 20.

''' 
Understanding:
Print Even numbers between 1 - 20


Approach:
while loop lopping thorough 20 
check if number n/2 ==0
'''

n = 1
print("\n===========================")
while n <= 20:
    if n % 2 ==0:
        print(f"{n} --> is an even number")
    n += 1

# Print the sum of numbers from 1 to 50 using a while loop.

'''
Understanding:
- sum of all numbers between 1 and 50 
- Use While loop specifically

Approach:
Looping through 1 to 50 while summing each number before incrementing.
'''

print("\n===========================")

n = 1
sum = 0

while n <= 50:
    sum += n
    n += 1
print(f"The sum of numbers from 1 to 50 is: {sum}")

print("\n===========================")


# Print the multiplication table of a given number (e.g., 5) up to 10.

'''
Understanding:
Print the tables of given number up to 10 only.

Approach:
loop though n upto 10 and multiply in each loop before incrementing
'''

n = 2

i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

# Print numbers from 10 to 1 in reverse order.

'''
Understanding:
- Reverse Printing from 10
'''

print("\n===========================")
num = 10

while num >= 0:
    print(num)
    num -= 1

# Print all numbers from 1 to 100 that are divisible by both 3 and 5.

'''
Understanding:
Print only numbers that are divisible by either 3 or 5 
range of number is 1 to 100

Approach:
num % 3 == 0 or num % 5 == 0 --> print(num)
'''
print("\n===========================")

num = 1

while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    num += 1

# Skip printing the number 4 and 7 from 1 to 10 using

'''
Problem Statement:
Print all number except 4 and 7 
number range should 1 - 10
'''
print("\n===========================")

num = 1

while num <= 10:
    if num == 4 or num == 7:
        num += 1
        continue
    print(num)
    num += 1


# Find the factorial of a number using a while loop

'''
Problem Statement:
Print fact of 

'''
print("\n===========================")
findFactOf = 6 #5x4x3x2x1
fact = 1
i = 1

# while findFactOf >= 1:
while i <= findFactOf:
    fact *= i
    i +=1
print(f"Factorial of {findFactOf} is {fact}")

# Print the square of numbers from 1 to 10 in this format:
print("\n===========================")

num = 1

while num <= 10:
    print(f"{num}^2 = {num**2}")
    num += 1


# Count how many digits are in a number using a while loop.
print("\n===========================")
num = 123456
count = 0

while num >0:
    num //= 10
    count += 1
print(count)


# Reverse a number using while loop
print("\n===========================")
num = 12345
reversedNum = 0

print("Number before reversing :",num)
while num > 0:
    rem = num % 10
    reversedNum = reversedNum * 10 + rem
    num //= 10
print(f"Reversed number is : {reversedNum}")

# Sum of digits of a number
print("\n===========================")
num = 1234
sum = 0
print("Given number :", num)

while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
print("The sum of numbers is :", sum)

# Check if a number is a palindrome
print("\n===========================")

givenNumber = 12121 #12121
original = givenNumber
reverseNumber = 0

while givenNumber > 0:
    rem = givenNumber % 10
    reverseNumber = reverseNumber * 10 + rem
    givenNumber //= 10

if original == reverseNumber:
    print(f"{original} - is a palindrome")
else:
    print(f"{original} - is not a palindrome")


'''
Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one
penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for
the number of days. Display a table showing what the salary was for each day. Finally, the program should display the total
pay at the end of the period. All output should be displayed as a dollar amounts and not as the number of pennies.
'''

print("\n==============================")
days = int(input("Enter the number of days: "))

day = 1
salary = 1  # in pennies
total = 0   # total in pennies

print("\nDay\tSalary (in dollars)")
print("==============================")

while day <= days:
    dollars = salary / 100  # convert pennies to dollars
    print(f"{day}\t${dollars:.2f}")
    total += salary
    salary *= 2  # double the salary for next day
    day += 1

total_dollars = total / 100
print("\n==============================")
print(f"Total pay after {days} days is: ${total_dollars:.2f}")