def searchR(nums, left, right, target):
    # Base case:
    if(right <= left):
        if(left == right and nums[left] == target):
            return [left, left]
        else:
            return [-1, -1]
    
    center = (left + right)//2
    
    # Case 1: center of sublist is equal to target
    if nums[center] == target:
        rslt = []
        a,b = searchR(nums, left, center - 1, target), searchR(nums, center + 1, right, target)
        
        if a[0] < center and a[0] != -1:
            rslt.append(a[0])
        else:
            rslt.append(center)
            
        if b[1] > center:
            rslt.append(b[1])
        else:
            rslt.append(center)
            
        return rslt
    
    # Case 2: center of sublist is not equal to target
    else:
        # Target is left of center
        if target < nums[center]:
            return searchR(nums, left, center - 1, target)
        else:
            return searchR(nums, center + 1, right, target)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return searchR(nums, 0, len(nums)-1, target)