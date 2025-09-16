A = [3, 5, 1, 2, 1, 2]
n = len(A)
reverse= []

for i in range(n - 1, -1, -1): 
    reverse.append(A[i])

print(reverse)
