import numpy as np

# matrix multiplication
# matrix A(n x k) * matrix B(k x m) = matrix C(n x m)

# general method
# Time Complexity : O(n^3), cubic time
def multiply_matrix(a, b):
    output = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                output[i][j] += a[i][k] * b[k][j]
    return output


# Time Complexity : subcubic time(less than n^3)
def strassen_algorithm(a, b):
    if len(a) == 1 and len(b) == 1:
        return a * b
    
    divide_size = len(a) // 2

    a11 = a[:divide_size, :divide_size]
    a12 = a[:divide_size, divide_size:]
    a21 = a[divide_size:, :divide_size]
    a22 = a[divide_size:, divide_size:]

    b11 = b[:divide_size, :divide_size]
    b12 = b[:divide_size, divide_size:]
    b21 = b[divide_size:, :divide_size]
    b22 = b[divide_size:, divide_size:]

    p1 = strassen_algorithm(a11, (b12 - b22))
    p2 = strassen_algorithm((a11 + a12), b22)
    p3 = strassen_algorithm((a21 + a22), b11)
    p4 = strassen_algorithm(a22, (b21 - b11))
    p5 = strassen_algorithm((a11 + a22), (b11 + b22))
    p6 = strassen_algorithm((a12 - a22), (b21 + b22))
    p7 = strassen_algorithm((a11 - a21), (b11 + b12))

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

# 3x3
a = np.random.randint(1, 9, (4, 4))
# 3x3
b = np.random.randint(1, 9, (4, 4))
# 3x3
output = multiply_matrix(a, b)
print(output)

output = strassen_algorithm(a, b)
print(output)