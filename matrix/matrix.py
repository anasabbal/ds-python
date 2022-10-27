from typing import List , Tuple, Callable

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    # return the size of matrix
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row

    return num_rows, num_cols

def make_matrix(num_rows: int, num_cols: int,
                entry_fn : Callable[[int, int], float]):
    #Creates a matrix given the number of rows and columns,and a generator function."""
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """Creates an nxn identity matrix"""
    return make_matrix(n,n,lambda i,j:1 if i == j else 0)

print(identity_matrix(5))
