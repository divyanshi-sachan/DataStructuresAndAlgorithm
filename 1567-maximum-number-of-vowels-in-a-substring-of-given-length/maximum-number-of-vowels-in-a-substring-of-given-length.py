class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        V = {'a','e','i','o','u','A','E','I','O','U'}
        current_vowel_count = 0
        window = s[:k]
        for ch in window:
            if ch in V:
                current_vowel_count+=1
            max_vowel = current_vowel_count
        for i in range(k,len(s)):
            if s[i] in V:
                current_vowel_count+=1
            if s[i-k] in V:
                current_vowel_count-=1
            max_vowel = max(max_vowel, current_vowel_count)
        return max_vowel

            