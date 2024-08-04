# from itertools import permutations

# def reciprocal(number):
#     try :
#         if number == 0:
#             raise ZeroDivisionError ("can't divide by zero")
#         elif number %2 != 0:
#             raise ValueError("the number is Odd")
#         else :
#             reciprocal = 1/number
#             return reciprocal
#     except ZeroDivisionError as z :
#         return z
#     except ValueError as v :
#         return v


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# # for num in numbers:
# #     result = reciprocal(num)
# #     print(result)


# from itertools import permutations


# from itertools import permutations


# def function(a, b, c):
#     string_numbers = [str(a), str(b), str(c)]
#     # By converting the permutations generator to a list, you can iterate over it multiple times to find both the maximum and minimum numbers.
#     perm = list(permutations(string_numbers))

#     max_number = max(int("".join(p)) for p in perm)

#     min_number = min(int("".join(p)) for p in perm)

#     difference = max_number - min_number

#     return difference, max_number, min_number

# result1 = function(4, 2, 8)
# print(result1)

from calculator.my_functions import (
    sum_numbers,
    subtract_numbers,
    divide_numbers,
    multiply_numbers,
)

def convert_file_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [ line.strip() for line in lines]

file_path = "python\input.txt"
lines = convert_file_to_list(file_path)
print(lines)


def write_list_to_file(output_file, data):
    with open(output_file, 'w') as file:
        for line in data:
            file.write(line + '\n')


data =["line1","line2","line3","line4"] 
data.append("line5")
output_file = "python\output.txt"

write_list_to_file(output_file, data)


def calc(operation, a, b):
    try:
        if operation == "0":
            return sum_numbers(a, b)
        elif operation == "1":
            if a == 0 or b == 0:
                raise ValueError("subtracting zero from Number")
            return subtract_numbers(a, b)
        elif operation == "2":
            if a==0 or b == 0:
                raise ZeroDivisionError("can't divide with zero")
            return divide_numbers(a, b)
        elif operation == "3":
            if a==0 or b == 0:
                raise ValueError("Multiply with Zero")
            return multiply_numbers(a, b)
        else:
            raise ValueError("Invalid operation")
    except ValueError as v:
        return v
    except ZeroDivisionError as z:
        return z


operation = "0"
a = 10 
b = 20
result = calc(operation, a, b)
print(result)
operation = "1"
a = 10 
b = 20
result = calc(operation, a, b)
print(result)
operation = "2"
a = 10 
b = 20
result = calc(operation, a, b)
print(result)
operation = "3"
a = 10 
b = 20
result = calc(operation, a, b)
print(result)
