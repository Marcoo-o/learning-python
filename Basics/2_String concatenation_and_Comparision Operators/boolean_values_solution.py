# Base
username = "admin"
min_length = 8
actual_length = len("Really_Secure_Super_Password!")

# Exercises:
#
# Write your own python code, that...
# 1.) Creates a variable with the name "$input_password" and set its value to a password of your choice.
# 2.) Creates a variable with the name "$is_admin", which checks if the length of "$username" equals to the length of "admin".
# 3.) Prints the result of this check.

input_password = "New_Super_Secret_Password"
is_admin = len(username) == len("admin")

print("The result of this check is:")
print(is_admin)