## Password Brute Force Tool

This Python script is a simple password brute force tool designed to check if a given password is present in a list of common passwords. It reads a list of common passwords from a file, hashes each password, and then compares the hashed values to the hashed actual password to check for a match. If a match is found, it suggests changing the password as it is considered easily guessable.

### Prerequisites
- Python 3.x
- hashlib library

### Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Place the list of common passwords in a file named `common_password_list.txt` in the same directory as the script.
4. Define the actual password you want to check by modifying the `actual_password` variable in the script.
5. Run the script by executing the following command in your terminal or command prompt:

```bash
python password-cracker.py
```

### Note

- The script uses the SHA1 hashing algorithm to hash the passwords. You can modify the `hash` function to use a different hashing algorithm if needed.
- The common password list should contain one password per line.

