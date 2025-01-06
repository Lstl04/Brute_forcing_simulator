import itertools
import string
import time

charset = string.ascii_letters + string.digits
capital_charset = string.ascii_uppercase
lowercase_charset = string.ascii_lowercase
digits = string.digits



def bruteforce(password):
    start = time.time()
    for char in charset:
        for guess in itertools.product(charset, repeat=len(password) - 1):
            guess = char + ''.join(guess)
            if(guess == password):
                print(f"done password found: {guess}")
                end = time.time()
                tim = f"time elapsed: {(end - start)} seconds"
                print(tim)
                return
    

def dir_bruteforce(password):
    start = time.time()
    with open('10-million-password-list-top-1000000.txt', 'r') as file:
        for line in file:
            word = line.strip()
            if word == password:
                print(f"password found in database: {word}")
                end = time.time()
                tim = f"time elapsed: {(int)(end - start)} seconds"
                print(tim)
                return
    with open('xato-net-10-million-passwords.txt', 'r') as file:
        for line in file:
            word = line.strip()
            if word == password:
                print(f"password found in database: {word}")
                end = time.time()
                tim = f"time elapsed: {(int)(end - start)} seconds"
                print(tim)
                return
    with open('list.txt', 'r') as file:
        for line in file:
            word = line.strip()
            if word == password:
                print(f"password found in database: {word}")
                end = time.time()
                tim = f"time elapsed: {(int)(end - start)} seconds"
                print(tim)
                return

    
    print("Didn't find anything! Password is safe")
    end = time.time()
    tim = f"time elapsed: {(int)(end - start)} seconds"
    print(tim)
    return

