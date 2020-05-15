class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = dict()
        
        for num in nums:
            if num in tracker:
                tracker.pop(num)
            else:
                tracker[num] = False
        
        for elem in tracker:
            return elem