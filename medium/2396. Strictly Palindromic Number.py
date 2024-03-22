class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert_to_base(num, base):
            if num == 0:
                return "0"
            digits = []
            while num:
                digits.append(str(num % base))
                num = num // base
            digits.reverse()
            return "".join(digits)

        for base in range(2, n - 1):
            converted = convert_to_base(n, base)
            if converted != converted[::-1]:  # Check if the string is not a palindrome
                return False
        return True
