#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  charCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      
  print("Lines :", lineCount)
  print("Words :" , wordCount)
  print("Characters :", charCount)

if __name__ == '__main__':
  main()
