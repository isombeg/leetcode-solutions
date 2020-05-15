class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        
        for index in range(len(nums)):
            if target - nums[index] in hashtable:
                return [
                    hashtable[target - nums[index]],
                    index
                ]
            
            else: hashtable[nums[index]] = index