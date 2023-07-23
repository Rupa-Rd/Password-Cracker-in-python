# Importing necessary libraries
import hashlib



# Function to read the most common_passwords
def common_passwords(url) :
    try:
       with open(url,'r') as f : # Opening the common_password_list file
           common_passwords_file = f.readlines()
           f.close()
    except Exception as e : # Throws an exception if there is a error in reading file
        print("Error in reading the common passwords file!!",e)
        exit()
    return common_passwords_file # returning the file contents


# Hashing all the passwords in common_passwords
def hash(common_password_file) :
    result = hashlib.sha1(common_password_file.encode()) # Hashing the password
    return result.hexdigest()


# Using bruteforce method to check the passwords
def bruteforce(guess_password_list, actual_password_hash) :
    
    for guess_password in guess_password_list : # Iterating through the passwords
        #print(guess_password,actual_password_hash)    
        if guess_password == actual_password_hash : # Checking whether the guesspassword matches the actual password
            print("Hey!, Your Password is : ", actual_password, 
                  "\nPlease change it, it was easy to guess it :)")
            exit()




url = 'common_password_list.txt'
# Defining a actual password
actual_password = '12345'
# Creating a hash for the actual password
actual_password_hash = hash(actual_password)

# Reading the common_password list
common_password = common_passwords(url)
guess_password_read = [x.replace('\n','') for x in common_password ]
guess_password_list = [hash(x) for x in guess_password_read]

# Running the brutforce attack
bruteforce(guess_password_list,actual_password_hash)

# If password couldn't able to find
print("Hey!, I couldn't guess your password :(")
