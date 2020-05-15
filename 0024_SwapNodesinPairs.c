/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode 
        *a = calloc(1, sizeof(struct ListNode)),
        *b = calloc(1, sizeof(struct ListNode)),
        *newHead = calloc(1, sizeof(struct ListNode));
    
    if(head == NULL)
        return NULL;
    else if(head->next == NULL)
        return head;
    
    a = head;
    b = head->next; newHead = head->next;
    
    while(a != NULL && b != NULL){
        // Reverse the connection
        a->next = b->next;
        b->next = a;
        
        if(a->next == NULL)
            return newHead;
        else if(a->next->next != NULL){
            b = a->next;
            a->next = b->next;
            a = b;
            b = b->next;
        }
        else return newHead;
    
    }
    
    return newHead;
}

