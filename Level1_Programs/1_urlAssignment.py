import os
import re
from urllib.request import urlopen

wordsList = []

def urlReader(url=None):
    global wordsList

    with urlopen(url) as lines:
        for line in lines:
            line_words = line.split()
            wordsList.append('\n')
            for word in line_words:
                wordsList.append(word)

def fileWriter(wordList):
    with open('urlAssignment.txt', 'w') as f:
        for _ in wordList:
            #print(_)
            if _ != '\n':
                f.write(_.decode('utf-'))
                f.write(' ')
            else:
                f.write(_)

def main():
    print('Start of program')
    urlReader('http://sixty-north.com/c/t.txt')
    #print(wordsList)
    fileWriter(wordsList)
    print('End of program')


if __name__ == '__main__':
    main()