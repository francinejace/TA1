# This program will count the sum of the digits from a given input string digits.

# Function
def digits(string):
    sum = 0
    for char in string:
        if char.isdigit():
            sum += int(char)
    return sum

# Main Function
def main():
    string = input('Enter a string of numbers: ')
    print(f'Sum of digits: {digits(string)}')
    
main()