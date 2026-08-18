class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        # O(n)
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        # O(m)
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            else:
                hashmap[char] = 1

        for val in hashmap.values():
            if val == 0:
                continue
            else:
                return False
        else:
            return True



        