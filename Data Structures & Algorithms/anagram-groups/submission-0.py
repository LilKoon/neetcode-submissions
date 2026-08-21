class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            chars = list(s)
            n = len(chars)

            for i in range(n):
                for j in range(0, n-i-1):
                    if chars[j] > chars[j+1]:
                        chars[j], chars[j+1] = chars[j+1],chars[j]
            
            key = ''.join(chars)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
    


            