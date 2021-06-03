fp = open("text.py", encoding="UTF-8")
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

# The number of words with a comma: cntWordsG
# The number of words without a comma: cntWords+cntStr
