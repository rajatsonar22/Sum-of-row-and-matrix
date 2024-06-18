# practical
x = int(input("Enter the nummber of rows:"))
y = int(input("Enter the number of coulmns:"))

matrix = []
print("Enter the coefficients of the matrix:")
for i in range(x):
    row =[]
    for j in range(y):
        row.append(int(input()))
    matrix.append(row)

print("Sum of eack row:")
for i in range(x):
    row_sum = sum(matrix[i])
    print("\nSum of row", i , "is",row_sum)

print("\nSum of each columb:")
for j in range(y):
    col_sum = sum(matrix[i][j] for i in range(x))
    print("The sum of coumumn",j,"is",col_sum)
