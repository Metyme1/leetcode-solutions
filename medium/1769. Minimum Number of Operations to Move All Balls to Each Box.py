class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        arr = []
        for i in range(n):  # Iterate over each position
            count = 0
            for j in range(n):  # Calculate distance from all '1's to position i
                if boxes[j] == '1':
                    count += abs(j - i)  # Add the distance from j to i
            arr.append(count)
        return arr
