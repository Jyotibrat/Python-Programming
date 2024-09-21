# Program to multiply matrices

# Function to multiply two matrices A and B
def matrix_multiply(A, B):
    # Initialize the result matrix with zeros
    result = [[0] * len(B[0]) for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices A and B
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Multiply matrices A and B
result = matrix_multiply(A, B)

# Print the resulting matrix
for r in result:
    print(r)