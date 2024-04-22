from collections import deque


from collections import deque


def findTheWinner(n, k):
    queue = deque(range(1, n + 1))

    # Continue until only one element remains in the deque
    while len(queue) > 1:
        # Manually rotate the queue k-1 times
        for _ in range(k - 1):
            # Pop from front and push to the back
            queue.append(queue.popleft())
        # Remove the k-th element
        queue.popleft()

    # The last remaining element is the winner
    return queue[0]


n = 6
k = 5
result = findTheWinner(n, k)
print("The winner is:", result)
