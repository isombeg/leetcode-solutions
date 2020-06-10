/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let colSet = new Set(), rowSet = new Set();
    
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(matrix[i][j] === 0){
                rowSet.add(i);
                colSet.add(j);
            }
            
        }
    }
    
    for(let item of rowSet){
        for(let i = 0; i < matrix[0].length; i++){
            matrix[item][i] = 0;
        }
    }
    
    for(let item of colSet){
        for(let i = 0; i < matrix.length; i++){
            matrix[i][item] = 0;
        }
    }
};