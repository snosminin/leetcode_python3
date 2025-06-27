class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s, map_t = {}, {}

        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = i
            if t[i] not in map_t:
                map_t[t[i]] = i

            if map_s[s[i]] != map_t[t[i]]:
                return False

        return True