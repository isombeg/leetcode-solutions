class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while not(right <= left):
            center = (left + right)//2
            
            # Base case: Center of sublist is the element
            if(nums[center] == target):
                return center
            
            if(target < nums[center]):
                right = center - 1
            else:
                left = center + 1
            
        if(nums[left] == target):
            return left
        elif(target < nums[left]):
            return left
        else:
            return left + 1
            