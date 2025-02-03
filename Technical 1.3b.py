# This program will display the numbers from 1 to a given number
# that is aligned to the left. (Nested while loop)

# Function
def left_aligned_numbers(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end='')
            j += 1
        print()
        i += 1
        
# Main Function
def main():
    n = int(input('Enter a number: '))
    left_aligned_numbers(n)
    
main()