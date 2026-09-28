class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned+=char.lower()
        print(cleaned)
        i = 0
        j = len(cleaned)-1
        while i < j:
            print(cleaned[i]," " ,cleaned[j])
            if cleaned[i]!=cleaned[j]:
                return False
            i+=1
            j-=1
        return True
        
            

        