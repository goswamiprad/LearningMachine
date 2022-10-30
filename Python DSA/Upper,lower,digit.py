def readfile():
    f=open("poem.txt","r")
    s=f.read()
    L1=len(s)
    print("Contents of the file poem.txt are:\n")
    print(s)
    print("\nSize of the file is=",L1,"Bytes")

def countchar():
    f1=open("poem.txt","r")
    alpha,lcase,ucase,digit,sp=0,0,0,0,0
    space,vowel,consonant=0,0,0
    for line in f1:
        words=line.split()
        space=space+len(words)-1
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    digit=digit+1
                if(letter.isalpha()):
                    alpha=alpha+1
                    if(letter in ['a','e','i','o','u','A','E','I','O','U']):
                        vowel=vowel+1
                    else:
                        consonant=consonant+1
                if(letter.isupper()):
                    ucase=ucase+1
                if(letter.islower()):
                    lcase=lcase+1
                if(letter.isalnum()==False):
                    sp=sp+1

    print("Alphabets::",alpha)
    print("Uppercase::",ucase)
    print("Lowercase::",lcase)
    print("Vowels::",vowel)
    print("Consonants::",consonant)
    print("digits::",digit)
    print("Special character::",sp)
    print("Space::",space)

            
readfile()
countchar()