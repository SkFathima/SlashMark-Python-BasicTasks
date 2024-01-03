import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")

    min_length = 3
    passwords = []
    for i in range(1, num_passwords + 1):
        length = int(input(f"Enter the length of Password #{i}: "))
        while length < min_length:
            print("Minimum length of password should be", min_length)
            length = int(input(f"Enter the length of Password #{i}: "))

        password = generate_password(length)
        passwords.append(password)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i}: {password}")

if __name__ == "__main__":
    main()
