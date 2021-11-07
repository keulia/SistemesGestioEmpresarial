import regex 

def numberPatrones (txt):
    twoZero = len(regex.findall(r'00', txt , overlapped=True))
    oneZeroOne = len(regex.findall(r'101', txt , overlapped=True))
    abc = len(regex.findall(r'abc', txt , overlapped=True))
    ho = len(regex.findall(r'ho', txt , overlapped=True))
    print("total of detected patterns: ",twoZero+oneZeroOne+abc+ho)


txt = input("Enter some text: ")

numberPatrones(txt.lower());