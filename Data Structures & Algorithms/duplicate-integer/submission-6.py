class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #Using a Hash Set we can search, add, and remove elements really fast.
         #creating a hashset
        hashset = set()

         #going through all input values in hashset

        for n in nums:
            if n in hashset: #if duplicate return true
                return True
                #if no duplicate add more items to the element
            hashset.add(n)
        return False