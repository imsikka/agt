def create_sparse_matrix(rows, cols, non_zero_entries):
    sparse_matrix = {(i, j): value for (i, j, value) in non_zero_entries if value != 0}
    return sparse_matrix

def transpose_sparse_matrix(matrix):
    transposed_matrix = {(j, i): value for (i, j), value in matrix.items()}
    return transposed_matrix

def print_matrix(matrix):
    max_row = max(row for row, _ in matrix.keys()) + 1
    max_col = max(col for _, col in matrix.keys()) + 1

    for i in range(max_row):
        for j in range(max_col):
            print(matrix.get((i, j), 0), end=" ")
        print()

# Example usage:
rows = 3
cols = 4
non_zero_entries = [(0, 1, 2), (1, 0, 3), (1, 2, 4)]

# Create sparse matrix
sparse_matrix = create_sparse_matrix(rows, cols, non_zero_entries)

# Print original matrix
print("Original Matrix:")
print_matrix(sparse_matrix)

# Transpose the matrix
transposed_matrix = transpose_sparse_matrix(sparse_matrix)

# Print transposed matrix
print("\nTransposed Matrix (Lexicographic Order):")
print_matrix(transposed_matrix)
