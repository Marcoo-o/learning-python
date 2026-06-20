# Base
min_length = 8
username = "admin"

# To make this series more interesting I will try continuously to build a little story around these lessons.
# Let's start. A user is trying to login to the admin account. We will have to validate against our password policy.
# So there will not be just one condition/statement but several. According to our policy the password is too short.
input_username = "admin"
input_password = "123"

# 1. Condition: Is the entered user the admin user?
is_correct_user = input_username == username
# Since "admin" equals to "admin" this statement is fulfilled.

# 2. Condition: Is the entered password long enough?
is_valid_len = len(input_password) >= min_length
# The comparison 3 >= 8 will return false, so one statement is not matched.

# To check for both statements simultaneously we need the logical operator 'and'
access_granted = is_correct_user and is_valid_len
# The 'and' operator only returns true if both conditions are true. In any other case it will return false.

print("Will the access be granted?")
print(access_granted)
# Since one statement is false the truth value will be false.

# Additional logical operators:
# and - Only returns true if both statements are true
# or  - Whenever there is a true in a statement it will return true
# not - Does negate the truth value (true -> false) and vice versa.


# Exercises:
#
# Write your own python code, that…
# 1.) Creates a variable with the name ip_blocked and set its value to "False".
# 2.) Creates a second variable with the name is_local_network and set its value to "True".
# 3.) Creates a third variable with the name allow_connection. It should only return true, if the
#     ip-address is NOT blocked AND the network is a local network.
# 4.) Returns the result of allow_connection via print(). 