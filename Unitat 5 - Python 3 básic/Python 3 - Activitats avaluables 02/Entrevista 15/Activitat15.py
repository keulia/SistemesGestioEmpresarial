import pyperclip
import sys

n = len(sys.argv)

forbiddenList = []
if n > 1:
    forbiddenFilePath =  sys.argv[1];
    f = open(forbiddenFilePath, "r")
    for x in f:
          forbiddenList.append(x.strip());

text = input("Please enter a text to copy:");
for forbiddenWord in forbiddenList:
    index = text.find(forbiddenWord);
    if index != -1:
        censorredWord = '';
        for i in range(len(forbiddenWord)):
            censorredWord = censorredWord + '*';
        text = text.replace(forbiddenWord, censorredWord)
pyperclip.copy(text)