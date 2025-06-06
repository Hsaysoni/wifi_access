import hashlib
import json
import os

DATA_FILE = "user_hashes.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def hash_password(email, password):
    combo = (email + password).encode()
    return hashlib.sha256(combo).hexdigest()

def main():
    data = load_data()
    while True:
        email = input("Enter your email ID: ").strip()
        password = input("Enter your password: ")
        hash_val = hash_password(email, password)
        data[email] = hash_val
        save_data(data)
        print(f"Hash for your password: {hash_val}")

        reuse = input("Do you want to reuse it? (yes/no): ").strip().lower()
        if reuse != "yes":
            break

    print("\nPassword hash retrieval:")
    email = input("Enter your email ID: ").strip()
    password = input("Enter your password: ")
    hash_val = hash_password(email, password)
    if email in data and data[email] == hash_val:
        print(f"Your password hash: {hash_val}")
    else:
        print("Email and password do not match our records.")

if __name__ == "__main__":
    main()
 
 