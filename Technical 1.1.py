# Function
def count_characters(string):
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0
    for char in string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
    return vowels, consonants, spaces

# Main Function
def main():
    string = input('Enter a string: ')
    vowels, consonants, spaces = count_characters(string)
    print(f'Vowels: {vowels}')
    print(f'Consonants: {consonants}')
    print(f'Spaces: {spaces}')
    print(f'Others: {len(string) - vowels - consonants - spaces}')

main()