/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    // Making sure number doesn't repeat itself
    let myMap = new Map();
    let curr;
    
    // Processing each new number
    while(n != 1){
        console.log(n);
        // Checking whether we've already seen number
        if(myMap.has(n))
            return false;
        
        // Logging in the number
        myMap.set(n, false);
        // Processing new number
        curr = 0;
        while(n != 0){
            curr += Math.pow(n % 10, 2);
            n = Math.floor(n / 10);
        }
        
        n = curr;
    }
    
    return true;
};