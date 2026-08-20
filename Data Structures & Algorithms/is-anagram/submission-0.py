class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s == t:
            return True

        lists = list(s)
        listt = list(t)
        lists.sort()
        listt.sort()

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if lists[i] != listt[i]:
                    return False
            return True
