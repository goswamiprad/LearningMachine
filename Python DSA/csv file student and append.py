import csv
def enterdata():
    f=open("stud1.csv","a",newline='')
    w=csv.writer(f)
    l=["RollNO","Name","Total","Percentage"]
    w.writerow(l)
    n=int(input("Enter no. of students:"))
    for i in range(n):
        r=int(input("\nEnter roll no::"))
        name=input("Enter name::")
        m1=int(input("Enter marks in Eng::"))
        m2=int(input("Enter marks in Phy::"))
        m3=int(input("Enter marks in Chem::"))
        m4=int(input("Enter marks in Maths::"))
        m5=int(input("Enter marks in CS::"))
        tot=m1+m2+m3+m4+m5
        per=tot/5
        rec=[r,name,tot,per]
        w.writerow(rec)
    f.close()

def display():
    f=open("stud1.csv","r")
    st=csv.reader(f)
    for i in st:
        print(i)
    f.close()

while True:
    print("\nMenu")
    print("1. Enter Data")
    print("2. Display Data")
    print("3. Exit")
    ch=int(input("Enter choice::"))
    if ch==1:
        enterdata()
    if ch==2:
        display()
    if ch==3:
        break

        