import string
import random

def token_gen(size=12):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(size))

if __name__ == '__main__':
    size = input("Enter the size of the token: ")
    print(token_gen(int(size)))
    
    from cryptography.fernet import Fernet
    new_key = Fernet.generate_key()
    print(new_key)