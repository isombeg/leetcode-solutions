/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let myMap = new Map();
    let rslt = new Array();
    
    for(let i = 0; i < nums.length; i++){
        if(myMap.has(nums[i]))
            myMap.delete(nums[i]);
        else myMap.set(nums[i], false);
    }
    //console.log(myMap);
    
    for(let [key,value] of myMap)
        rslt.push(key);
    
    return rslt;
};