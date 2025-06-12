
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashset1 = defaultdict(int)
        hashset2 = defaultdict(int)


        for i in s:
            hashset1[i] += 1
        
        for k in t:
            hashset2[k] += 1

        return hashset1 == hashset2
    

# Time: O(n)

# Space: O(n)