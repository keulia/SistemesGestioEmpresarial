"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Exercise 15
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
import pyperclip
import sys

n = len(sys.argv)

forbiddenList = []
if n > 1:
    forbiddenFilePath =  sys.argv[1]; # We define the path of the forbidden list word
    f = open(forbiddenFilePath, "r")
    for x in f:
          forbiddenList.append(x.strip()); # We are adding the words into the forbidden list

text = input("Please enter a text to copy:");
for forbiddenWord in forbiddenList:
    index = text.find(forbiddenWord); 
    if index != -1:
        censorredWord = '';
        for i in range(len(forbiddenWord)): # Here we are changing each character of the word to a *
            censorredWord = censorredWord + '*'; 
        text = text.replace(forbiddenWord, censorredWord) # We are replacing the forbidden words for the new modified words
pyperclip.copy(text)

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