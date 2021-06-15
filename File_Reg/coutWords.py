import os

def countWords(nameFile):
    source = os.getcwd()+'\\temp\\'+nameFile+'.txt'
    fp = open(source, encoding="UTF-8")
    line = fp.readline()
    lineN = " "
    cntWords = 0
    cntWordsG = 0
    cntStr = 0
    while len(line) != 0:
        for i in line:
            if i == ",":
                cntWordsG = cntWordsG + 1
            if i == " ":
                cntWords = cntWords + 1
        lineN = line[::-1]
        line = fp.readline()
        cntStr = cntStr + 1
    fp.close()
    string = f"The number of words with a comma: {cntWordsG} \nThe number of words without a comma: {cntWords+cntStr}"
    return string

# if __name__ == '__main__':
#     print(countwords("temp//text.py"))

# The number of words with a comma: cntWordsG
# The number of words without a comma: cntWords+cntStr
