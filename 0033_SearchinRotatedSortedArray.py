class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        
        left, right = 0, len(nums)-1
        center = right//2
        while not (nums[center] == target or right <= left):
            
            
            # Case 1: center is greater than left, smaller than right
            if(nums[center] >= nums[left] and nums[center] <= nums[right]):
                print("Case1")
                if(target < nums[center]):
                    right = center - 1
                else:
                    left = center + 1
            
            # Case 2: center is greater than left and right
            elif(nums[center] >= nums[left] and nums[center] >= nums[right]):
                print("Case2")
                if(target >= nums[left] and target < nums[center]):
                    right = center - 1
                else:
                    left = center + 1
                    
            # Case 3: center is smaller than left and right
            else:
                print('Case3')
                if target > nums[center] and target <= nums[right]:
                    left = center + 1
                else:
                    right = center - 1
            
            center = (left + right)//2
            
        
        if nums[center] == target:
            return center
        
        return -1
        
            
        