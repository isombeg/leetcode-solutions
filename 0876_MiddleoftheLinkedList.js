/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    // Special case: list has 1 or less entries, therefore head is middle
    if(head == null || head.next == null)
        return head;
    
    // Initialize to pointers to use runner approach
    let p = head, q = head.next;
    
    while(q != null){
        if(q.next == null)
            return p.next;
        
        q = q.next.next;
        p = p.next;
    }
    
    return p;
};