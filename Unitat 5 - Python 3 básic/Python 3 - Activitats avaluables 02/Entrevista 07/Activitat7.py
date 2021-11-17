"""
1 - Recieve the name of 2 different documentos
2 - Make 2 functions -"isPalindrome" "isPrime"

3 - Prime function - that number will get divided until half of that number. so if: 10 it will get divided until 5
  - if number divided by 2 = 0 then number isn't prime
  - if number isn't divisable by anything expect 0 and 1, number is prime

 4 - Palindrome function - turn the number of the line in the opposite order, starting from the right
   - compare original number with new number
   - if they equal the same then isPalindrome = true

"""


import sys
import doctest

"""
print("Introduce the file we will read from: ")
textFile = sys.argv

"""
def isPrime(lines):
    if int(lines)%2==0:

def isPalindrome(lines):
    # Copy in reverse
    reverse = lines[::-1]
    if int(lines) == int(reverse):
        return true

countPalindrome = 0
# With r we are opening the document in a reading mode
# Using with will close automatically our text document once we are done with it
with open('readme.txt', 'r') as f:
    lines = f.readlines()
    if isPalindrome(f) == true:
        countPalindrome+1

# With w we will be writting in the text
with open('readme.txt', 'w') as f:
    f.write()
    f.write('/n')
