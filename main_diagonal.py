def diagonal_sum(matrix,rows,columns):
    sum=0
    for i in range(rows):
        sum+=matrix[i][i]
    return sum
arr=list(map(int,input().split()))
r=arr[0]
c=arr[1]
matrix=[]
counter=2
for i in range(r):
    matrix.append(arr[counter:counter+r])
    counter+=r
print(diagonal_sum(matrix,r,c))
