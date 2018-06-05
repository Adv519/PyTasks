import os

class stringDemo:
    def __init__(self, testString):
        this.testString = testString

    def getString(self):
        return this.testString

    def setString(self, paramString=None):
        this.testString =

    def printString(self, paramString=None):
        print(paramString)

    def setRawString(self, rawString):
        this.testString = rawString

    def printRawString(self):
        return this.testString

def main():
    stringDemoObj = stringDemo('ForTesting')

    ##printing the string
    print("First Print Statement")
    stringDemoObj.printString(stringDemoObj.getString())

    ##Using backslash in the string
    stringDemoObj.setRawString('This string contains a backslash \\')

    ##printing the string
    print("Second print statement")
    stringDemoObj.printString(stringDemoObj.getString())

    ##Using raw strings, an alternative to double backslash
    stringDemoObj.setRawString(r'C:\Users\JnaneswarVanga')

    ##Printing raw string
    print("Third print statement")
    stringDemoObj.printRawString()


    print("End of main")


if __name__ == '__main__':
    main()