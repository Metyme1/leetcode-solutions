# def find_substrings_with_same_start_end(string):
#     substrings = []
#     n = len(string)
    
#     count=0
    
#     for i in range(n):
#         for j in range(i , n):
#             if string[i] == string[j]:
#                 substring = string[i:j+1]
#                 if substring  not in substrings:
#                     substrings.append(substring)
#                     count +=1

#     return substrings,count

def find_substrings_with_same_start_end(string):
    substrings = []
    n = len(string)
    start = 0

    while start < n:
        end = start
        while end < n:
            if string[start] == string[end]:
                substring = string[start:end+1]  # Append substring from index start to end (inclusive)
                substrings.append(substring)
            end += 1
        start += 1

    return substrings

string = "xyzyz"
result = find_substrings_with_same_start_end(string)
print(result)  # Output: ['yzy']

string = "xyx"
result = find_substrings_with_same_start_end(string)
print(result)  # Output: ['xyx']