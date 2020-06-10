/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    digits[digits.length - 1]++;
    
    for(let p = digits.length - 1; p > 0; p--){
        if(digits[p] == 10){
            digits[p] = 0;
            digits[p - 1]++;
        }
    }
    
    if(digits[0] === 10){
        digits[0] = 0;
        digits.unshift(1);
    }
    
    return digits
};