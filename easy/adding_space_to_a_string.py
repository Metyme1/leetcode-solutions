class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result =[]
        for i,char in enumerate(s):
            if i in spaces:
                result.append(' ')
            result.append(char)
        return ''.join(result)