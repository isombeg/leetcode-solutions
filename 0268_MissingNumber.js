/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let i, exp_sum = 0, real_sum = 0;
    for(let i = 0; i < nums.length; i++){
        exp_sum += i + 1;
        real_sum += nums[i];
    }
    
    return exp_sum - real_sum;
};