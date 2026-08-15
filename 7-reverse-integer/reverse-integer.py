class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31-1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x!=0:
            a = x%10
            x//=10
            if rev > (max-a)//10:
                return 0
            rev = rev * 10 + a
        return rev*sign



        