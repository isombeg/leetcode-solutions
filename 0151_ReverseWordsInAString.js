/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    if(s.length === 0)
        return s;
    
    let new_s = '';
    let r = s.length, l = s.length;
    
    while(l > 0){
        
        while(r > 0 && s[r-1] === ' '){
            r--;
        }
        if(r <= 0){
            break;
        }
        
        l = r - 1;
        while(l > 0 && s[l-1] !== ' '){
            l--;
        }
        
        console.log(l,r);
        new_s += new_s.length ? ' ' + s.slice(l,r) : s.slice(l,r);
        r = l - 1;
    }
    
    return new_s;
    
};