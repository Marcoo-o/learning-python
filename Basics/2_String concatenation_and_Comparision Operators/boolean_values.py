# Base
username = "admin"
min_length = 8
actual_length = len("Really_Secure_Super_Password!")

# A variable which stores a boolean value (true or false)
# The right term of "=" is a comparison of greater than (>=) equals.
is_valid_length = actual_length >= min_length

print("Does the password meet the policy requirements?")
print(is_valid_length)

# Summary:
# 
# Whenever there is a comparison the evaluation of this term will be a boolean.
# It can only take two defined states: true and false.
#
# Possible comparison combinations:
# a > b, a < b         a is greater than b, a is less than b
# a >= b, a <= b       a is greater equals than b, a is less equal than b
# a == b, a != b       a equals to b, a is not equal to b

# Exercises:
#
# Write your own python code, that...
# 1.) Creates a variable with the name input_password and set its value to a password of your choice.
# 2.) Creates a variable with the name is_admin, which checks if the length of username equals to the length of "admin".
# 3.) Prints the result of this check.