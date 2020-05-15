/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    if(nums.length <= 1)
        return false;
    
    myMap = new Map();
    for(let i = 0; i < nums.length; i++){
        if(myMap.has(nums[i])){
            return true;
        }
        else myMap.set(nums[i], false);
    }
    
    return false;
};