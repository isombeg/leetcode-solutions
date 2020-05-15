/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let sumOfNums = 0, sumOfSet = 0, occ = 0, i;
    let myMap = new Map();
    for (i = 0; i < nums.length; i++){
        if(!myMap.has(nums[i])){
            myMap.set(nums[i], false);
            sumOfSet += nums[i];
        }
        else occ++;
            
        sumOfNums += nums[i];
        
    }
    return (sumOfNums - sumOfSet)/occ;
};