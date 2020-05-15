#include <limits.h>

#define ASCII_0 48
#define ASCII_A 65
#define ASCII_MINUS_SIGN 45
#define ASCII_PLUS_SIGN 43
#define SPACE 32



int myAtoi(char * str){
    int x = 0;
    
    while(str[0] == SPACE)
        str++;
    
    if(str[0] >= ASCII_A)
        return x;
    
    else if(str[0] == ASCII_MINUS_SIGN){
        
        str++;
        while(str[0] != 0){
            if(str[0] >= ASCII_A || str[0] < ASCII_0) break;
            else if(x < INT_MIN/10 || (x == INT_MIN/10 && str[0]-ASCII_0 > 8))
                return INT_MIN;
            else x = 10*x - ((str[0] - ASCII_0));
            str++;
        }
        return x;
    }
    
    else{
        
        if(str[0] == ASCII_PLUS_SIGN) str++;
        
        while(str[0] != 0){
            if(str[0] >= ASCII_A || str[0] < ASCII_0) break;
            else if(x > INT_MAX/10 || (x == INT_MAX/10 && str[0]-ASCII_0 > 7))
                return INT_MAX;
            else x = 10*x + ((str[0] - ASCII_0));
            str++;
        }
        return x;
    }
}

