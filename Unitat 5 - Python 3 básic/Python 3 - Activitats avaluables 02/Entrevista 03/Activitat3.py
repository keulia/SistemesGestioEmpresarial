txt = input("Enter a text")

twoZero = 0
oneZeroOne = 0
abc = 0
ho = 0

if txt.find("00"):
    twoZero+=1
elif(txt.find("101")):
    oneZeroOne+=1
elif(txt.find("abc")):
    abc+=1
elif(txt.find("ho")):
    ho+=1


print("00: ",twoZero)
print("101: ",oneZeroOne)
print("abc: ",abc)
print("ho: ",ho)