class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dict1 = {'}':'{',']':'[',')':'('}
        for char in s :
            if char in  '({[':
                st.append(char)
            else:
                if not st or st[-1]!= dict1[char]:
                    return False
                st.pop()
        return len(st) == 0
            


        