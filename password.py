import random
import string

def generate_password(length, digits=True, uppercase=True, lowercase=True, symbols=True):
    characters = ''
    
    if digits:
        characters += string.digits
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if symbols:
        characters += string.punctuation
    
    if not characters:
        print('error')
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("length: "))
include_digits = input("digits? (y/n): ").lower() == 'y'
include_uppercase = input("uppercase? (y/n): ").lower() == 'y'
include_lowercase = input("lowercase? (y/n): ").lower() == 'y'
include_symbols = input("symbols? (y/n): ").lower() == 'y'

generated_password = generate_password(
    password_length, 
    digits=include_digits, 
    uppercase=include_uppercase, 
    lowercase=include_lowercase, 
    symbols=include_symbols
)

if generated_password:
    print(f'generated password: {generated_password}')


