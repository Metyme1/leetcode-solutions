def can_remove_ones(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Mark rows and columns for flipping
    flip_rows = set()
    flip_cols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                flip_rows.add(i)
                flip_cols.add(j)

    # Step 2: Flip marked rows and columns
    for row in flip_rows:
        for j in range(cols):
            matrix[row][j] = '0' if matrix[row][j] == '1' else '1'

    for col in flip_cols:
        for i in range(rows):
            matrix[i][col] = '0' if matrix[i][col] == '1' else '1'

    # Step 3: Check if there are any remaining '1's
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                return False

    return True
matrix =[[0,1,0]]