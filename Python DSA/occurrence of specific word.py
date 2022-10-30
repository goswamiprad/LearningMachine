def readfile():
    f1=open("train.txt","r")
    content=f1.read()
    print("The Content of the file is::\n")
    print(content)

def countword():
    f1=open("train.txt","r")
    cnt1,cnt2,cnt3,cnt4=0,0,0,0
    userword=input("Enter your word::")

    for line in f1:
        words=line.split()
        for i in words:
            if(i=="the"):
                cnt1=cnt1+1
            if(i=="train"):
                cnt2=cnt2+1
            if i in ["Train","train"]:
                cnt3=cnt3+1
            if(i==userword):
                cnt4=cnt4+1

    print("No. of occurrence of the word (the) is::",cnt1)
    print("No. of occurrence of the word (train) is::",cnt2)
    print("No. of occurrence of the word (Train or train) is::",cnt3)
    print("No. of occurrence of the word",userword, "is::",cnt4)

readfile()
countword()