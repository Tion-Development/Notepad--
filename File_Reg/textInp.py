import os

def fileText(temp):
    sourse = temp
    fp = open(temp, encoding="UTF-8")
    l = fp.readline()
    text = l
    while len(l) != 0:    
        l = fp.readline()
        text += fp.readline()
    return text
