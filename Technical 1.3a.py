# Function
def right_aligned_numbers(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(i):
            print(j + 1, end='')
        print()

# Main Function
def main():
    n = int(input('Enter a number: '))
    right_aligned_numbers(n)
    
main()