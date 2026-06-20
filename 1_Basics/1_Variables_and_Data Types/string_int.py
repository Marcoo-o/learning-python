# To get started we will start off simple by definitions.
# 
# String: A sequence of characters used to represent text. (e.g.: Letters, Numbers, or Symbols)
# Integer: A data type used to represent whole numbers (e.g.: 0, 1, 2, -3, -4)
#
# Although you can represent numbers both ways, you should always consider using them directly as integers.

# A variable which stores a string
target_password = "Really_Secure_Super_Password!"

# The len() function helps us to determine the character length of an object (here: string).
# A variable which stores an integer
password_length = len(target_password)

# The str() function helps us to convert an object to a string.
# The print() function print the values of objects to a stream (here: stdout).
# Output of the results
print("The examined password is:")
print(target_password)
print()
print("The length of the password is:")
print(str(password_length) + " Characters")

# As you can see variables doesn't need to be declared with a
# specific type. The type is first determined at runtime.


# Exercises:
#
# Write your own python code, that…
# 1.) Creates a variable with the name username and set its value to "admin"
# 2.) Creates a second variable with the name min_length and set its value to 8 (int).
# 3.) Finds out how many characters there are in username and show the result via print().