def solution(A, B):
    l = len(A)

    A.sort()
    B.sort(reverse=True)

    temp1 = 0
    for i in range(l):
        temp1 += A[i] * B[i]

    A.sort(reverse=True)
    temp2 = 0

    for i in range(l):
        temp2 += A[i] * B[i]
        
    return min(temp1, temp2)
