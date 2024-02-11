class Solution:
    def judgeSquareSum(self, c: int) -> bool:
       left = 0
       right = int(math.sqrt(c))
       while left <= right:
           sum_of_squares = left**2 + right**2
           if sum_of_squares == c:
               return True
           elif sum_of_squares < c:
               left += 1
           else:
               right -= 1
       return False

        