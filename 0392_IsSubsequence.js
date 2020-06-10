/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let a = 0, b = 0;
    
    while(b < t.length && a < s.length){
        if(s[a] === t[b]){
            a++;
        }
        b++;
    }
    
    if(a === s.length)
        return true;
    else return false;
};