#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char* frame;
    int qty;
} Stack;

Stack* createStack();
void push(Stack* s, char key);
void pop(Stack* s);
char top(Stack* s);
int isEmpty(Stack* s);

bool isValid(char* s) {
    if(s[0] == 0) return 1;
    
    Stack* a = createStack(strlen(s));
    
    push(a, s[0]);
    
    for(int i = 1; s[i] != 0; i++){
        if(s[i] - top(a) > 0 && s[i] - top(a) <= 2)
            pop(a);
        else push(a, s[i]);
    }
    
    return isEmpty(a);
}

Stack* createStack(int n){
    Stack* r = (Stack*)calloc(1,sizeof(Stack));
    r->frame = (char*)calloc(n, sizeof(char));
    r->qty = 0;
    return r;
}

void push(Stack* s, char key){
    s->frame[s->qty++] = key;
}

void pop(Stack* s){
    s->qty--;
}

char top(Stack* s){
    if(!isEmpty(s))
        return s->frame[s->qty - 1];
    return 0;
}

int isEmpty(Stack* s){
    return s->qty == 0;
}