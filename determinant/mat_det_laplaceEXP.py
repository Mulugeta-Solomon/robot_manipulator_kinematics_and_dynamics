import numpy as np

def determinant(A):
    # Check that the matrix is square
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix must be square to compute determinant")

    # Compute the determinant using the Laplace expansion
    if n == 1:
        # If the matrix is 1x1, the determinant is the single element
        return A[0,0]
    elif n == 2:
        # If the matrix is 2x2, the determinant is given by ad - bc
        a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
        return a*d - b*c
    else:
        # For matrices of dimension 3 or greater, expand along the first row
        det = 0
        for i in range(n):
            # Compute the submatrix by removing the i-th column and first row
            submatrix = A[1:, np.arange(n) != i]
            # Compute the determinant of the submatrix using recursion
            subdet = determinant(submatrix)
            # Add the contribution to the determinant
            det += (-1)**i * A[0,i] * subdet
        return det

# Test the function
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(determinant(A))  # Output: 0
