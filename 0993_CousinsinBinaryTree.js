/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    if(root.val === x || root.val === y)
        return false;
    
    let parents = new Array(), children = new Array(); // arrays for level-order traversal
    let targ_parent;
    let flag = false;
    parents.push(root);
    
    while(parents.length !== 0){
        let i;
        // checking for leftmost target
        for(i = 0; i < parents.length; i++){
            if(parents[i].left !== null){
                if(parents[i].left.val == x || parents[i].left.val == y){
                    if(flag)
                        return true;
                    flag = true;
                    targ_parent = i;
                }
                children.push(parents[i].left);
            }
        }
        
        if(flag){
            
            if(parents[targ_parent].right !== null){
                if(parents[targ_parent].right.val == x || parents[targ_parent].right.val == y){
                    return false
                }
            }
        }
        for(i = 0; i < parents.length; i++){
            if(parents[i].right !== null){
                if(parents[i].right.val == x || parents[i].right.val == y){
                    if(flag)
                        return true;
                    flag = true;
                }
                children.push(parents[i].right);
            }
        }
        if(flag)
            return false;
        
        parents = children;
        children = new Array();
        flag = false;
    }
    
};