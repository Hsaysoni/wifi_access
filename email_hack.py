import time
import random
import string
import sys

def show_progress(step, duration=2):
    for percent in range(0, 101, random.randint(8, 16)):
        sys.stdout.write(f"\r{step:<32} {percent:3d}%")
        sys.stdout.flush()
        time.sleep(duration / 10)
    sys.stdout.write(f"\r{step:<32} 100%\n")
    sys.stdout.flush()
    time.sleep(0.5)

def retrieve_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    email = input("Enter user email address: ")
    print(f"\n[INFO] Initializing recovery process for: {email}\n")
    time.sleep(1)

    show_progress("Connecting to authentication server", 1.2)
    show_progress("Synchronizing user directory", 1.5)
    show_progress("Validating user credentials", 1.8)
    show_progress("Decrypting password hash", 2.2)
    show_progress("Finalizing recovery", 1.0)

    password = retrieve_password()
    print("\n[RESULT] Password recovery successful.")
    print(f"[USER]   {email}")
    print(f"[PASSWORD]   {password}\n")

if __name__ == "__main__":
    main()
    print("you can not be a hacker by copying my code")
