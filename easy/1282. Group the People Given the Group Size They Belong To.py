class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        
        for person,size in enumerate(groupSizes):
            groups[size].append(person)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result
        