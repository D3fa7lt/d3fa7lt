# Encrypt password using hash 

import hashlib 

h = hashlib.new("SHA256") 
h.update(b"Enter the password ") 

print(h.hexdiegst())
