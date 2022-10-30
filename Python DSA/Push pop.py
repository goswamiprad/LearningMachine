def isempty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def push(stack):
    data=int(input("\nEnter a number to push::"))
    stack.append(data)
    print("After pushing",data,"stack status is:")
    display(stack)

def pop(stack):
    if isempty(stack):
        print("Stack is Empty")
    else:
        val=stack.pop()
        print("\nDeleted item was:",val)
        print("After popping",val,"Stack status is:")
        display(stack)

def peek(stack):
    if isempty(stack):
        return "Underflow"
    else:
        top=len(stack)-1
        return stack[top]

def display(stack):
    if isempty(stack):
        print("stack is empty")
    else:
        top=len(stack)-1
        print(stack[top],"<==(Top)")
        while(top>0):
            print(stack[top-1],"<==")
            top=top-1
        print()

stack=[]
top=None
while True:
    print("\nMenu for stack implementation")
    print("1. Push")
    print("2. Pop")
    print("3. Display Peek")
    print("4. Display stack")
    print("5. Quit")
    ch=int(input("Enter your choice::"))
    if ch==1:
        push(stack)
    elif ch==2:
        pop(stack)
    elif ch==3:
        val=peek(stack)
        if val=="Underflow":
            print("Stack is Empty")
        else:
            print("Top item:",val)
    elif ch==4:
        print("Stack status is::")
        display(stack)
    elif ch==5:
        break
