# Part 1: for loop
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
# Part 2: if- else statement
numbers = [5, -3, 0, 8, -7]
for num in numbers:
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
        # Part 3: while loop
        index = 0
        while index < len(numbers):
            if numbers[index] == 0:
                break
            if numbers[index] % 2 == 0:
                print("Even number:")
            else:
                print("Odd number:")
            index += 1