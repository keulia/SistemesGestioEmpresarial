"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Ejercicio 3
|＿＿＿＿＿＿＿＿＿＿＿|
⠀⠀⠀⠀⠀⠀(\__/) ||
⠀⠀⠀⠀⠀⠀(•ㅅ•) ||
⠀⠀⠀⠀⠀⠀/ 　 づ

Autor: Cassandra Sowa Candela ♡ ´･ᴗ･ `♡
2ºDAM
Octubre 2021

⠀                                                 ⠀∩∩
                                                ♡(｡･x･)♡  

   ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄                                                                     ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄ 
   █▒▒░░░░░░░░░▒▒█                                                                     █▒▒░░░░░░░░░▒▒█
    █░░█░░░░░█░░█                                                                       █░░█░░░░░█░░█
 ▄▄  █░░░▀█▀░░░█  ▄▄                                                                 ▄▄  █░░░▀█▀░░░█  ▄▄
█░░█ ▀▄░░░░░░░▄▀ █░░█                                                               █░░█ ▀▄░░░░░░░▄▀ █░░█

*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡
"""
import hashlib

# Function to encrypt
def encryptPass(password):
    return hashlib.sha256(password.encode()).hexdigest();

# Example with a list
list = [
{"username1",encryptPass("password1")},
{"username2",encryptPass("password2")},
{"username3",encryptPass("password3")},
{"username4",encryptPass("password4")},
{"username5",encryptPass("password5")}]

# Example with a dictionary
dict = {
    "cassandra": encryptPass("password1"),
    "napsta": encryptPass("password2"),
    "marlon": encryptPass("password3"),
    "vida": encryptPass("password4"),
    "george": encryptPass("password5"),

}
# Check if the password is the same
print (dict["cassandra"] == encryptPass("casspass"))
print (dict["cassandra"] == encryptPass("password1"))
# Shows the encrypted password
print (dict["napsta"])
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