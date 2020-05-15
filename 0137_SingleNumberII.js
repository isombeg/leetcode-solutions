/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let myMap = new Map();
    let sumOfSet = 0, sumOfNums = 0;
    
    for(let i = 0; i < nums.length; i++){
        if(!myMap.has(nums[i])){
            myMap.set(nums[i], false);
            sumOfSet += nums[i];
        }
        
        sumOfNums += nums[i];
    }
    
    return (3*sumOfSet - sumOfNums)/2;
};