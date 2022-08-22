def bitwiseAnd(N, K):
    # Write your code here
    res = -1
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            z = i&j
            if z < K and z > res:
                res = z
    return res


bitwiseAnd(955, 236)