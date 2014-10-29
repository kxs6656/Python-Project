import os
import sys
charClass = -1
lexeme=[]
nextChar = ''
lexLen = 0
token = 0
nextToken = 0
#Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = 999
#Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MUL_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

i = 0
count = 0
index = 0

def getChar():
    global index
    global charClass
    global nextChar
    with open('Front.txt','r') as InputFile:
        InputFile.seek(index)
        nextChar = InputFile.read(1)
        index+=1
        if nextChar:
            if nextChar.isalpha():
                charClass = LETTER;
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN
        else:
            charClass = EOF


def addChar():
    global lexeme
    global count
    if len(lexeme)<=100:
        lexeme.append(nextChar)
        count+=1
    else:
        print ("Error: lexeme is too long.")
       

def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()

        
def lex():
    global nextToken
    global i
    global count
    lexLen = 0
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
        i = 0
        count = 3
    print ("Next token is : "+str(nextToken)+",Next lexeme is :  "+str("".join(lexeme[i:count])))
    i = count
    return nextToken


def lookup(nextChar):
    global nextToken
    if nextChar=='(':
        addChar()
        nextToken = LEFT_PAREN
    elif nextChar == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif nextChar == '+':
        addChar()
        nextToken = ADD_OP
    elif nextChar == '-':
        addChar()
        nextToken = SUB_OP
    elif nextChar == '*':
        addChar()
        nextToken = MUL_OP
    elif nextChar == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken



def main():
    global EOF
    global nextToken
    if open('Front.txt','r'):
        getChar()
        while True:
            lex()
            if nextToken == EOF:
                break
main()        
