#include <limits.h>

int isPalindrome(int x){
    int q, rev = 0;
    
    if(x < 0) return 0;
    else if(x < 10) return 1;
    else if(x%10 == 0) return 0;
    
    while(x != 0 && (rev < INT_MAX/10 || rev == INT_MAX/10 && x <= 7)){
        q = x % 10;
        x /= 10;
        
        if(x == rev) return 1;
        rev = 10*rev + q;
        if(x == rev) return 1;
    }
    
    return 0;
}

