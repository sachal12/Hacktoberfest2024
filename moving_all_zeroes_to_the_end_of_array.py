# Python Program to move all zeros to the end

A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
B = [0] * n
j = 0
count = 0

for i in range(n):
	if A[i] != 0:
		B[j] = A[i]
		j += 1
	else:
		count += 1

while count > 0:
	B[j] = 0
	count -= 1
	j += 1

for i in range(n):
	A[i] = B[i]

for i in range(n):
	print(A[i], end=' ') # Print the array


