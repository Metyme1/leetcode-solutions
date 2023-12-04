# def find_row_intersection(matrix):

#     common_elements = set(matrix[0])

#     for num in matrix[0]:
#         for i in range(1, len(matrix)):
#             if num not in matrix[i]:
#                 common_elements.discard(num)

#     return common_elements

# print (min((find_row_intersection([[1,9,3,4],[7,8,9,3],[3,4,5,9]]))))



# def longest_common_subsequence(array1, array2):
#     i, j = 0, 0
   

#     while i < len(array1) and j < len(array2):
#         lcs = []
#         if array1[i] == array2[j]:
#             lcs.append(array1[i])
#             i += 1
#             j += 1
#         elif array1[i] > array2[j]:
            
#             j+=1
#         else:
#             i+=1
    

#     return lcs


# # Example usage:
# array1 = [1, 2, 4, 6, 8]
# array2 = [2, 4, 6, 8, 10]
# result = longest_common_subsequence(array1, array2)
# print(result)
def remove_ones(grid):
    rows = set()
    cols = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                rows.add(i)
                cols.add(j)

    if len(rows) == 0 or len(cols) == 0:
        return True

    if len(rows) * len(cols) % 2 == 0:
        return True

    return False


def remove(grid):
    n = len(grid)
    m = len(grid[0])

    for i in range(m):
        if grid[0][i] == 1:
            for j in range(n):
                grid[j][i] = 1 - grid[j][i]

    for i in range(1, n):
        row_sum = sum(grid[i])
        if row_sum != 0 and row_sum != m:
            return False

    return True


print(remove([[1,1,0],[0,0,0],[0,0,0]])) 