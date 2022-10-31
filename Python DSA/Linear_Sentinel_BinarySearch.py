def Linsearch(arr,x):    
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def Sentsearch(arr,x):
    l = len(arr)
    arr.append(x)
    i = 0
    while(arr[i]!=x):
        i = i+1
    if(i!=l):
        return i
    else:
        return -1

def Binsearch(arr,KEY):
    n = len(arr)
    for i in range(n - 1):
       for j in range(0, n - i - 1):
           if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Roll nos in sorted way for Binary Search")
    for i in range(len(arr)):
        print(arr[i])
    beg= 0
    end= len(arr)-1
    c= 0
    while(beg<=end):
        c=(beg+end)//2	#mid of the array is obtained
        if(KEY<arr[c]):
            end= c-1#search the left sub list
        elif(KEY>arr[c]):
            beg= c+1#search the right sub list
        else:
             return c

    return -1 
print("\nHow many Students are there?")
n = int(input())
array = []
i=0
for i in range(n):
    print("\n Enter roll number: ")
    item = int(input())
    array.append(item)

print("The Roll Numbers of Students are ...\n")
print(array)
while(True):
    print("Main Menu")
    print("\n 1. Linear Search")
    print("\n 2. Sentinel Search")
    print("\n 3. Binary Search")
    print("\n 4. EXIT")
    print("\n Enter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Linsearch(array,key)
        if(location !=-1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice == 2):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Sentsearch(array,key)
        if(location !=-1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice==3):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Binsearch(array,key)
        if(location !=-1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice==4):
        print("Thank you for using this program");
        break
        
