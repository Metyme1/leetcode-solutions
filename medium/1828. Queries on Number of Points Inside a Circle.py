class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:

        arr = []
        for q in queries:
            count = 0
            for p in points:
                if (pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2)) <= pow(q[2], 2):
                    count += 1
            arr.append(count)
        return arr
