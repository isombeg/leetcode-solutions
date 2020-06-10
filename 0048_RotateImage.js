/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    rot(matrix, 0);
    return matrix;
};

const rot = (matrix, x) => {
    let a, b;
    
    if(x >= (matrix.length - 1)/2)
        return;
    
    for(let i = 0; i < matrix.length - 2*x - 1; i++){
        // Upper row to right column
        a = matrix[x][x + i];
        b = matrix[x + i][matrix.length - 1 - x];
        matrix[x + i][matrix.length - 1 - x] = a;

        // Right column to lower row
        a = matrix[matrix.length - 1 - x][matrix.length - 1 - x - i];
        matrix[matrix.length - 1 - x][matrix.length - 1 - x - i] = b;
        
        // Lower row to left column
        b = matrix[matrix.length - 1 - x - i][x];
        matrix[matrix.length - 1 - x - i][x] = a;
        
        // Left column to upper row
        matrix[x][x + i] = b;
        
    }
    
    rot(matrix, x + 1);
}