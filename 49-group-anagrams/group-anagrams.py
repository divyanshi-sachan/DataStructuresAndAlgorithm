class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(s)
        return list(dict1.values())

        