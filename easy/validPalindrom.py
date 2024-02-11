s = input
class solution:
    def plaindrom(self, s: str)-> bool:
        newstr= ""
        for i in s:
            if i.isalnum():
                newstr +=i
        return newstr == newstr[::-1]