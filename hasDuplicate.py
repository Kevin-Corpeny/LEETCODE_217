class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return not (len(set(nums)) == len(nums)) #one line version
        
        valMap = {}
        for x in nums:
            if x not in valMap.keys():
                valMap[x] = 1
                continue
            return False
        return True
