/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    if(nums.length < 2)
        return nums;
    
    // p1 tracks leftmost 0 at all given times, p2 searches for non-zero elems
    let p1 = 0, p2, temp;
    
    // Searching for leftmost 0
    while(nums[p1] != 0 && p1 < nums.length)
        p1++;
    p2 = p1 + 1;
    
    while(p2 < nums.length){
        // Swap with leftmost 0 if p2 points to non-zero
        if(nums[p2] != 0){
            holder = nums[p1];
            nums[p1] = nums[p2];
            nums[p2] = holder;
            p1++;
        }
        
        p2++;
    }
    
    return nums
};