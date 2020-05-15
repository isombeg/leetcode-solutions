/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let myMap = new Map();
    
    for(let i = 0; i < nums.length; i++){
        if(!myMap.has(nums[i]))
            myMap.set(nums[i], false);
        else myMap.set(nums[i], true);
    }
    
    for(let [key, value] of myMap){
        if(value == false)
            return key;
    }
};