def count_repeated_substrings(s):
    n = len(s)
    unique_substrings = set()
    count = 0
    left = 0
    right = 1

    while left < n:
        while right < n and s[right] not in unique_substrings:
            unique_substrings.add(s[right])
            right += 1

        count += right - left - 1
        unique_substrings.remove(s[left])
        left += 1

    return count

# Example usage
test_cases = int(input())

for _ in range(test_cases):
    string = input()
    result = count_repeated_substrings(string)
    print(result)