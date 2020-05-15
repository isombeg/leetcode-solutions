#include <stdio.h>

int cont_area(int* a, int* b){
    //printf("left: %d \tright: %d \tdiff: %d\n", a, b, b-a);
    return (b-a) * (*a < *b ? *a : *b);
}

int shift(int* a, int* b){
    int *x = a, *y = b;
    
    while(*x == *y && x < y){
        x++; y--;
    }
    
    if(*x < *y) return 1;
    else if(*x > *y) return 0;
    else return -1;
}

int maxArea(int* height, int heightSize){
    int 
        area,
        shiftVal,
        maxArea = 0,
        *left = height,
        *right = height + heightSize - 1;
    
    while(left != right){
        area = cont_area(left, right);
        if(area > maxArea)
            maxArea = area;
        
        shiftVal = shift(left, right);
        
        if(shiftVal == 1) left++;
        else if(shiftVal == 0) right--;
        
        else{
            left++;
            while(left != right){
                area = cont_area(left, right);
                if(area > maxArea)
                    maxArea = area;
                left++;
            }
            break;
        }
    }
    
    return maxArea;
}

