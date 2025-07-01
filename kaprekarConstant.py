def kaprekar_constant(num):

    # Making sure the input is 4 digits only
    if num < 1000 or num > 9998 or len(set(str(num))) == 1:
        print("Please enter a valid 4-digit number with at least two different digits.")
        return

    steps = 0

    # Implementing Kaprekar Logic
    while num != 6174:
        digits = list(str(num))
        asc = int(''.join(sorted(digits)))
        desc = int(''.join(sorted(digits, reverse=True)))
        num = desc - asc
        print(f"{desc:04d} - {asc:04d} = {num:04d}")
        steps += 1

    print(f"Reached 'Kaprekar constant' 6174 in {steps} step(s)")

# Testing with a random 4-digit number => 3524
userInput = int(input("Enter a 4-digit number with at least two different digits: "))
kaprekar_constant(userInput)
