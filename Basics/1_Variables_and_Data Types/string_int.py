# A variable which stores a string
target_password = "Really_Secure_Super_Password!"

# A variable which stores an integer
password_length = len(target_password)

# Output of the results
print("The examined password is:")
print(target_password)
print()
print("The length of the password is:")
print(str(password_length) + " Characters")


# Summary:
# 
# As you can see variables doesn't need to be declared with a
# specific type. The type is first determined at runtime.
# 
# The len() function helps us to determine the character length of a string.
# The str() function helps us to convert non-string data types to a string.


# Exercises:
#
# Write your own python code, that...
# 1.) Creates a variable with the name username and set it's value to "admin"
# 2.) Create a second variable with the name min_length and set it's value to 8 (int).
# 3.) Find out how many characters there are in username and show the result via print().