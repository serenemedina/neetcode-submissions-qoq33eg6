class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset
        hashset = set()

        for n in nums:
     # first check if n is a duplicate, does it already exist in the hash set
            if n in hashset:
                return True

            # if not true, add the value to our hashset and continue
            hashset.add(n)
        return False # did not find any duplicates 
        