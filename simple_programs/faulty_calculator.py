#Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


operation = input(" + for Addition \n - for Substraction \n * for multiplication \n / for Division \n Enter input: ");

#45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

result = 0

if operation == "+":
    if first_number == 56 and second_number == 9:
        result = 77
    else:
        result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    if first_number == 45 and second_number == 3:
        result = 555
    else:
        result = first_number * second_number
elif operation == "/":
    if first_number == 56 and second_number == 6:
        result = 4
    else:
        result = first_number / second_number
else:
    print("Invalid operation.")

print(result)
