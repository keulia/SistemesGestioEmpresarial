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
    if not int(lines)%2==0: # If the number in that line isn't divisible by 2 do
        n = lines%2 # im adding that number divided by 2 so i can divide the number to a max of that answer
        d = 3 # So i start diving by 3 each line
        for x in int(n): # So it goes from X to half of that number
            if not lines%d==0: # starts by number divided by 3, if it's divisible return "false" if it is not divisible by any number return true
                if d == (n-1): # If d is the same number 
                    return True
                else:
                    d=d+1 # number that is used to divide increases by one for the next loop
            else:
                return False
    else:
        return False

def isPalindrome(lines):
    # Copy in reverse
    reverse = lines[::-1] # We reverse the order
    if lines == int(reverse): # If the reversed version is the same as the original then it will return true
        return true

countPalindrome = 0 # To count how many Palindrome numbers we have
countPrime = 0 # To count how many Prime numbers we have
# With r we are opening the document in a reading mode
# Using with will close automatically our text document once we are done with it

bothNUmbers = []
with open('readme.txt', 'r') as f:
    lines = f.readlines()
    if isPalindrome(f):
        countPalindrome+1
        if isPrime(f) == true:
            bothNUmbers.append(f)

    if isPrime(f) == true:
        countPrime+1

# With w we will be writting in the text
with open('readme.txt', 'w') as f:
    f.write('There are ',countPalindrome,' Palindrome numbers')
    f.write('/n')
    f.write('There are ',countPrime,' Prime numbers')
    f.write('/n')



