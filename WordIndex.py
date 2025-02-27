#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
    textFile = open("fish.txt", 'r')
  
    words = {} #create an empty dictionary
    lineNum = 0
  
    for line in textFile:
        lineNum = lineNum + 1
        wordList = line.split()
     
        for w in wordList:
            w = w.lower()
            w = w.replace("," , "")
            w = w.replace("." , "")


  
            if w in words:
                words[w].append(lineNum)
            else:
                words[w] = [lineNum]

    print(words)


if __name__ == '__main__':
  main()
