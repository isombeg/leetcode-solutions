/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    // Special case: array has 1 or 0 elems
    if(nums.length <= 1){
        return nums.length;
    }
    
    let a = 0, b = 1;
    while(b < nums.length){
        if(nums[a] == nums[b]){
            nums.splice(b,1);
        }
        else{
            a++;
            b++;
        }
    }
    
    // console.log(nums.length);
    return nums.length;
};