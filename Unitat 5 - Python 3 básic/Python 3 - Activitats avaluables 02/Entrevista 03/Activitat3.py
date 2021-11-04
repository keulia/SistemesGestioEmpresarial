txt = input("Enter some text")

twoZero = 0
oneZeroOne = 0
abc = 0
ho = 0
div1 = 1
div2 = 1
div3 = 1
div4 = 1

for c in txt:
    if txt.count("00"):
        twoZero+=1
        div1+=1
    elif(txt.count("101")):
        oneZeroOne+=1
        div2+=1
    elif(txt.count("abc")):
        abc+=1
        div3+=1
    elif(txt.count("ho")):
        ho+=1
        div4+=1
    else:
        print("No results!")

twoZero = twoZero/div1
oneZeroOne = oneZeroOne/div2
abc = abc/div3
ho = ho/div4
#OFC IT DOESNT WORK WTFFF

print("00: ",twoZero)
print("101: ",oneZeroOne)
print("abc: ",abc)twoZero = twoZero/div1
oneZeroOne = oneZeroOne/div2
abc = abc/div3
ho = ho/div4
abc = abc/div3
ho = ho/div4