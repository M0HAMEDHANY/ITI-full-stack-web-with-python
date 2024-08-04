#  1. Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string
def count_vowels (string): 
    count = 0
    for i in string.lower():
        if i in 'aeiou':
            count += 1
    return count

# print(count_vowels(input("Enter a string: ")))
print('--------------------------------------------------------------')

# 2. Write a function that accepts two arguments (length,start) to generate an array of a specific length filled with integer numbers increased by one from start.
def generate_array(length, start):
    arr = []
    for i in range(length):
        arr.append(start + i)
    return arr

# print(generate_array(int(input("Enter length: ")), int(input("Enter start: "))))
print('--------------------------------------------------------------')

# 3. Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output
def sort_numbers(numbers):
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    return ascending, descending


numbers_list = [10, 2, 33, 45, 5, 67]
ascending, descending = sort_numbers(numbers_list)
# print("Original list:" ,numbers_list)
# print("Ascending order:", ascending)
# print("Descending order:", descending)

print('--------------------------------------------------------------')

# 4. Write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is divisible by both return "FizzBuzz"
def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# fizz_buzz(9)
print('--------------------------------------------------------------')

#  5. Write a function which has an input of a string from user then it will return the same string reversed.
# using seq [start , stop , step]
def reverse_str(string):
    print(string[::-1])

# reverse_str("hello")
print('--------------------------------------------------------------')

# 6. Write a Python function that checks whether a passed string is palindrome or not.Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run {ignoring the spaces }.


def is_palindrome(string):
    cleaned_string = ''.join(string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

# print(is_palindrome("lol"))
# print(is_palindrome("train"))
# print(is_palindrome("hello"))
print("--------------------------------------------------------------")

# 7. Write a function that takes a string and prints the longest alphabetical ordered substring occured. For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu
def longest_alphabetical_substring(s):
    max_substring = current_substring = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            current_substring += s[i]
        else:
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = s[i]
            
    if len(current_substring) > len(max_substring):
        max_substring = current_substring
        
    print(f"Longest substring in alphabetical order is: {max_substring}")

longest_alphabetical_substring("abdulrahman")
longest_alphabetical_substring("abcabcdefg")
longest_alphabetical_substring("zyxwvutsrqponmlkjihgfedcba")
