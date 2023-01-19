class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        perms_set = set()
        for i in range(len(s) + 1 - k):
            perms_set.add(s[i : i + k])
        return len(perms_set) == 2 ** k

