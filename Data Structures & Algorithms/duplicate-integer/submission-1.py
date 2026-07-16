class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            hashtable[num] = hashtable.get(num, 0) + 1
        for num in hashtable:
            if hashtable[num] > 1:
                return True
        return False
