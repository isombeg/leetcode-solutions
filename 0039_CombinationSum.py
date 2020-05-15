def combine(nums, end, compliment, rslt, temp):
    
    # Base case: number at end of window is equal to compliment
    if compliment == 0:
        rslt.append(temp.copy())
        return rslt
    
    while nums[end] > compliment and end >= 0:
        end -= 1
        
    if(end < 0):
        return rslt
    else:
        for i in range(end,-1,-1):
            temp.append(nums[i])
            rslt = combine(nums, i, compliment - nums[i], rslt, temp)
            temp.pop()
        return rslt

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return combine(candidates, len(candidates) - 1, target, [], [])