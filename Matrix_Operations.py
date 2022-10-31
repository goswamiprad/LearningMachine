def add_matrix(A,B):
    result = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

    print("The Addition of Two Matrices...")
    for r in result:  
        print(r)
 
def sub_matrix(A,B):
    result = [[A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

    print("The Subtraction of Two Matrices...")
    for r in result:
        print(r)

def transpose(A):
    result = [[0 for col in range(col_num)] for row in range(row_num)]  
    for i in range(len(A)):  
       for j in range(len(A[0])):  
           result[j][i] = A[i][j]  
  
    print("Transposed Matrix A is ...")
    for r in result:  
        print(r)  

def transpose(B):
    result = [[0 for col in range(col_num)] for row in range(row_num)]  
    for i in range(len(B)):  
       for j in range(len(B[0])):  
           result[j][i] = B[i][j]  
  
    print("Transposed Matrix B is ...")
    for r in result:  
        print(r)  

def Mul_matrix(A,B):
    result = [[0 for col in range(col_num)] for row in range(row_num)]  
    for i in range(len(A)):  
        for j in range(len(B[0])):  
           for k in range(len(B)):  
               result[i][j] += A[i][k] * B[k][j]  
    print("Matrix Multiplication is ...")
    for r in result:  
        print(r)  
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
A = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        item = int(input("Enter the elements in first matrix: "))
        A[row][col]= item

print("The first matrix is...")
print(A)
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
B = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        item = int(input("Enter the elements in second matrix: "))
        B[row][col]= item

print("The second matrix is...")
print(B)
print("Program for Matrix Operations")
while(True):
    print(" 1. Addition of Two Matrices")
    print(" 2. Subtraction of Two Matrices")
    print(" 3. Multiplication of Two Matrices")
    print(" 4. Transpose of Matrix")
    print(" 5. Exit ")
    print(" Enter your choice: ")
    choice = int(input())
    if(choice == 1):
        add_matrix(A,B)
    elif(choice == 2):
        sub_matrix(A,B)
    elif(choice == 3):
        Mul_matrix(A,B)
    elif(choice == 4):
        transpose(A)
        transpose(B)
    else:
        print("Thanks for Using this program")
        break
