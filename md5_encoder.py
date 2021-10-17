#! usr/bin/env python3
# importing modules
import hashlib

# user input
str = input("Enter a string to convert into md5: ")

# converting into md5
enc = hashlib.md5(str.encode()).hexdigest()

# printing results

