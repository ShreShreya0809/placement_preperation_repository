def dun(A, B, a, b):
    # Appending B to A
    for i in B: A.append(i)
    A = list(set(sorted(A)))  # Remove duplicates and sort A

    B = A[len(A) - b:]  # Extract the last b elements as B
    A = A[:len(A) - b]  # Remove the last b elements from A
