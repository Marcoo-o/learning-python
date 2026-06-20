# Exercises:
#
# Write your own python code, that…
# 1.) Creates a variable with the name ip_blocked and set its value to "False".
# 2.) Creates a second variable with the name is_local_network and set its value to "True".
# 3.) Creates a third variable with the name allow_connection. It should only return true, if the
#     ip-address is NOT blocked AND the network is a local network.
# 4.) Returns the result of allow_connection via print().

ip_blocked = False
is_local_network = True
allow_connection = not ip_blocked and is_local_network

print("Will the access be granted?")
print(allow_connection)