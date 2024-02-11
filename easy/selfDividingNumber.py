class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        while left <= right:
            digits = str(left)
            for digit in digits:
                if digit == '0' or left % int(digit) != 0:
                    break
            else:
                arr.append(left)
            left += 1
        return arr


        