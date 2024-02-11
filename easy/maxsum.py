def maxSum(arr, n, k):
    l = 0
    r = k - 1
    max_sum = 0
    while r < n:
        sum1 = sum(arr[l:r+1])
        max_sum = max(max_sum, sum1)
        l += 1
        r += 1
    return max_sum

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    k = 2
    result = maxSum(arr, n, k)
    print(result)