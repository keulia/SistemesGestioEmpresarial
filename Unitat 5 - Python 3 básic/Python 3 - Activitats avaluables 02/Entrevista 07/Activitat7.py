"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Exercise 7
|＿＿＿＿＿＿＿＿＿＿＿|
⠀⠀⠀⠀⠀⠀(\__/) ||
⠀⠀⠀⠀⠀⠀(•ㅅ•) ||
⠀⠀⠀⠀⠀⠀/ 　 づ

Author: Cassandra Sowa Candela ♡ ´･ᴗ･ `♡
2ºDAM
November 2021

⠀                                                 ⠀∩∩
                                                ♡(｡･x･)♡  

   ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄                                                                     ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄ 
   █▒▒░░░░░░░░░▒▒█                                                                     █▒▒░░░░░░░░░▒▒█
    █░░█░░░░░█░░█                                                                       █░░█░░░░░█░░█
 ▄▄  █░░░▀█▀░░░█  ▄▄                                                                 ▄▄  █░░░▀█▀░░░█  ▄▄
█░░█ ▀▄░░░░░░░▄▀ █░░█                                                               █░░█ ▀▄░░░░░░░▄▀ █░░█

*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡
"""

from numpy import sqrt  # Import this for calculating mathematical operations

file = open("readme.txt")  # Open the input file
lines = file.read().splitlines() 
file.close()

prime_list = []      # List that stores prime numbers.
palindrome_list = [] # List that stores palindromic strings.


#for palindrome_list 
for i in range(len(lines)):
    a=len(lines[i])
    flag = 0
    for j in range(a):
        if(lines[i][j] != lines[i][a-j-1]):
            flag = 1
    if(flag == 0):
        palindrome_list.append(lines[i])
            
#for prime_list
def isPrime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True

for i in lines:
    i=int(i)
    if(isPrime(i)):
        prime_list.append(i)

#getting length of the common_list which can be checked which has less elements
q = 0
if(len(palindrome_list)<len(prime_list)):
    q=len(palindrome_list)
else:
    q=len(prime_list)

#common_list    
common_list = [] #common_list which contains both prime and palindrome-one
#checking equal items
for i in range(q):
    if(prime_list[i] == int(palindrome_list[i])):
        common_list.append(prime_list[i])

#to append common_list in file
with open('output.txt', 'a') as f:
    f.write(f"There are {len(palindrome_list)} palindromic numbers.\n")
    f.write(f"There are {len(prime_list)} prime numbers.\n")
    for i in common_list:
        f.write(str(i))
        f.write("\n")
f.close()
#open file and read contents of output.txt file
f = open("output.txt", "r")
print(f.read())
"""
*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡
⠀⠀⠀⠀°. ♡
⠀⠀⠀⠀. °
⠀⠀＿♡
⊂⊂ ・）
⠀/　 |
⊂＿__u

*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
"""