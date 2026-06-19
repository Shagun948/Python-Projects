import random
import string

print("===== Password Generator =====")

length = int(input("Enter the desired password length: "))

print("\nChoose Password Complexity:")
print("1. Letters Only")
print("2. Letters and Numbers")
print("3. Letters, Numbers, and Special Characters")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    characters = string.ascii_letters
elif choice == 2:
    characters = string.ascii_letters + string.digits
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Using default complexity.")
    characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)
